/* Hello World Example

   This example code is in the Public Domain (or CC0 licensed, at your option.)

   Unless required by applicable law or agreed to in writing, this
   software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
   CONDITIONS OF ANY KIND, either express or implied.
*/

// 看门狗错误 https://blog.csdn.net/weixin_42938082/article/details/122659057
#include <stdio.h>
#include <time.h>

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_spi_flash.h"

#include "lwip/timeouts.h"

#include "driver/gpio.h"
#include "driver/adc.h"
#include "esp_adc_cal.h"

#include "sdkconfig.h"

#include "cJSON.h"

#include "wifi_connect.h"
#include "mqtt_client_package.h"

#include "ssd1306.h"
#include "font8x8_basic.h"

#include "sensor/dth11.h"
#include "sensor/light.h"

typedef unsigned char byte;
typedef unsigned char uint8_t;

static const char* APP_TAG = "[APP]";
esp_err_t          ret     = ESP_OK;

static void print_chip_init_info();

void app_main(void)
{
    int   i = 0;
    char* now_time_srt[20];   // Time got
    float light_percent = 0.; // 光百分比

    // dth11 传感器数据
    DTH11_DATA dth11_data = {
        .temperature = 0.,
        .humidity    = 0.,
    };

    SSD1306_t dev;
    int       center, top, bottom;
    char      display_str[200];
    int       page = 0;

    cJSON* cjson_info = cJSON_CreateObject(); // json 根节点
    cJSON* cjson_data = cJSON_CreateObject(); // json 子节点 "data"
    char*  cjson_str  = "";                   // json 字符串

    char mac_addr[18]     = {0};
    byte base_mac_addr[6] = {0}; // 84:F7:03:39:9F:C8
    int  device        = 0;
    ret                   = esp_efuse_mac_get_default(base_mac_addr); // 本机 Mac 地址

    device = (base_mac_addr[3] << (sizeof(byte) * 2)) + (base_mac_addr[4] << (sizeof(byte))) + base_mac_addr[5];
    // ESP_LOGE(TAG, "Mac: %s", base_mac_addr);
    // ESP_LOGE(TAG, "Mac: %d:%d:%d", base_mac_addr[3], base_mac_addr[4], base_mac_addr[5]);
    // ESP_LOGI(TAG, "Mac: %d", device_id);
    // vTaskDelay(10000 / portTICK_PERIOD_MS);
    // esp_restart();


    struct tm now_time = {0};

    if (ret != ESP_OK)
    {
        ESP_LOGE(TAG, "Failed to get base MAC address from EFUSE BLK0. (%s)", esp_err_to_name(ret));
        ESP_LOGE(TAG, "Aborting");
        abort();
    }
    else
    {
        ESP_LOGI(TAG, "Base MAC Address read from EFUSE BLK0");
        snprintf(mac_addr, sizeof(mac_addr), "%02X:%02X:%02X:%02X:%02X:%02X",
                 base_mac_addr[0], base_mac_addr[1], base_mac_addr[2],
                 base_mac_addr[3], base_mac_addr[4], base_mac_addr[5]);
    }
    {
        ESP_LOGI(TAG, "INTERFACE is SPI");
        ESP_LOGI(TAG, "CONFIG_MOSI_GPIO = %d", CONFIG_MOSI_GPIO);
        ESP_LOGI(TAG, "CONFIG_SCLK_GPIO = %d", CONFIG_SCLK_GPIO);
        ESP_LOGI(TAG, "CONFIG_CS_GPIO	= %d", CONFIG_CS_GPIO);
        ESP_LOGI(TAG, "CONFIG_DC_GPIO	= %d", CONFIG_DC_GPIO);
        ESP_LOGI(TAG, "CONFIG_RESET_GPIO= %d", CONFIG_RESET_GPIO);
        spi_master_init(&dev, CONFIG_MOSI_GPIO, CONFIG_SCLK_GPIO, CONFIG_CS_GPIO, CONFIG_DC_GPIO, CONFIG_RESET_GPIO);
        ESP_LOGI(TAG, "Panel is 128x64");
        ssd1306_init(&dev, 128, 64);
        ssd1306_clear_screen(&dev, false);
        // ssd1306_contrast(&dev, 0xff);
        ssd1306_display_text_x3(&dev, 0, "Hello", 5, false);
    }

    app_init_adc();

    ssd1306_clear_screen(&dev, false);
    wifi_connect_sta();                                 // Init WiFi
    esp_mqtt_client_handle_t client = mqtt_app_start(); // MQTT client


    cJSON_AddNumberToObject(cjson_info, "device", device);
    // cJSON_AddStringToObject(cjson_info, "time", "");
    cJSON_AddNumberToObject(cjson_info, "date", 0);
    cJSON_AddNumberToObject(cjson_info, "time", 0);
    {
        cJSON_AddNumberToObject(cjson_data, "light", 0);
        cJSON_AddNumberToObject(cjson_data, "temperature", dth11_data.temperature);
        cJSON_AddNumberToObject(cjson_data, "humidity", dth11_data.humidity);
        cJSON_AddItemToObject(cjson_info, "data", cjson_data);
    }


    while (1)
    {
        page = 0;
        ssd1306_clear_screen(&dev, false);
        struct tm now_time = get_now_time();

        int date = (now_time.tm_year + 1900) * 10000 + (now_time.tm_mon + 1) * 100 + now_time.tm_mday;
        int time = now_time.tm_hour * 10000 + now_time.tm_min * 100 + now_time.tm_sec;

        cJSON_ReplaceItemInObject(cjson_info, "date", cJSON_CreateNumber(date));
        cJSON_ReplaceItemInObject(cjson_info, "time", cJSON_CreateNumber(time));

        strftime(now_time_srt, sizeof(now_time_srt), "%Y-%m-%d %H:%M:%S", &now_time);
        strftime(display_str, sizeof(display_str), "%Y-%m-%d", &now_time);
        ssd1306_display_text(&dev, page, display_str, strlen(display_str), false);
        strftime(display_str, sizeof(display_str), "%H:%M:%S", &now_time);
        page += 1;
        ssd1306_display_text(&dev, page, display_str, strlen(display_str), false);


        {

            light_percent = light_get_light() * 100;
            cJSON_ReplaceItemInObject(cjson_data, "light", cJSON_CreateNumber(light_percent));
            snprintf(display_str, sizeof(display_str), "light %.2f %%", light_percent);
            page += 2;
            ssd1306_display_text(&dev, page, display_str, strlen(display_str), false);
        }
        {
            dth11_data = dth11_get();
            if (dth11_data.temperature < 990 && dth11_data.humidity < 880)
            {
                cJSON_ReplaceItemInObject(cjson_data, "temperature", cJSON_CreateNumber(dth11_data.temperature));
                cJSON_ReplaceItemInObject(cjson_data, "humidity", cJSON_CreateNumber(dth11_data.humidity));
                snprintf(display_str, sizeof(display_str), "temp  %.2f oC", dth11_data.temperature);
                page += 2;
                ssd1306_display_text(&dev, page, display_str, strlen(display_str), false);
                snprintf(display_str, sizeof(display_str), "humi  %.2f %%", dth11_data.humidity);
                page += 2;
                ssd1306_display_text(&dev, page, display_str, strlen(display_str), false);
            }
        }
        {
            snprintf(display_str, sizeof(display_str), "i=%d, d=%-6.2f", 22, 9.2);
        }

        ESP_LOGI(TAG, "light:%.2f\t ", light_percent);
        ESP_LOGI(TAG, "Temp:%.2f℃ Humi:%.2fRH\n ", dth11_data.temperature, dth11_data.humidity);
        cjson_str = cJSON_Print(cjson_info);
        mqtt_publish_message(client, cjson_str);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}


void print_chip_init_info()
{
    ESP_LOGI(APP_TAG, "Startup..");
    ESP_LOGI(APP_TAG, "Free memory: %d bytes", esp_get_free_heap_size());
    ESP_LOGI(APP_TAG, "IDF version: %s", esp_get_idf_version());
    /* Print chip information */
    esp_chip_info_t chip_info;
    esp_chip_info(&chip_info);
    ESP_LOGI(APP_TAG, "Chip %s with %d CPU core(s), WiFi%s%s, ", CONFIG_IDF_TARGET,
             chip_info.cores,
             (chip_info.features & CHIP_FEATURE_BT) ? "/BT" : "",
             (chip_info.features & CHIP_FEATURE_BLE) ? "/BLE" : "");
    ESP_LOGI(APP_TAG, "silicon revision %d, ", chip_info.revision);
    ESP_LOGI(APP_TAG, "%dMB %s flash\n", spi_flash_get_chip_size() / (1024 * 1024),
             (chip_info.features & CHIP_FEATURE_EMB_FLASH) ? "embedded" : "external");
    ESP_LOGI(APP_TAG, "Minimum free heap size: %d bytes\n", esp_get_minimum_free_heap_size());
}