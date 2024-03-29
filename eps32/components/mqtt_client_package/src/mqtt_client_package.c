/* MQTT (over TCP) Example

   This example code is in the Public Domain (or CC0 licensed, at your option.)

   Unless required by applicable law or agreed to in writing, this
   software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
   CONDITIONS OF ANY KIND, either express or implied.
*/

// #include <stdio.h>
// #include <stdint.h>
// #include <stddef.h>
// #include <string.h>

// #include "esp_wifi.h"
// #include "esp_system.h"
// #include "nvs_flash.h"
// #include "esp_event.h"
// #include "esp_netif.h"

// #include "freertos/FreeRTOS.h"
// #include "freertos/task.h"
// #include "freertos/semphr.h"
// #include "freertos/queue.h"

// #include "lwip/sockets.h"
// #include "lwip/dns.h"
// #include "lwip/netdb.h"

// #include "esp_log.h"
// #include "mqtt_client.h"

// Custome
#include "mqtt_client_package.h"

void log_error_if_nonzero(const char *message, int error_code)
{
    if (error_code != 0)
    {
        ESP_LOGE(MQTT_TAG, "Last error %s: 0x%x", message, error_code);
    }
}

void mqtt_event_handler(void *handler_args, esp_event_base_t base, int32_t event_id, void *event_data)
{
    ESP_LOGD(MQTT_TAG, "Event dispatched from event loop base=%s, event_id=%d", base, event_id);
    esp_mqtt_event_handle_t event = event_data;
    esp_mqtt_client_handle_t client = event->client;
    int msg_id;

    switch ((esp_mqtt_event_id_t)event_id)
    {

    case MQTT_EVENT_CONNECTED: // 建立连接成功
        ESP_LOGI(MQTT_TAG, "MQTT_EVENT_CONNECTED");
        // printf("topic sub %s", event->topic);

        // msg_id = esp_mqtt_client_publish(client, "/plantsmate", mqtt_publish_data3, strlen(mqtt_publish_data3), 0, 0);
        // ESP_LOGI(MQTT_TAG, "sent publish successful, msg_id=%d", msg_id);

        // msg_id = esp_mqtt_client_subscribe(client, "/plantsmate", 0);
        // ESP_LOGI(MQTT_TAG, "sent subscribe successful, msg_id=%d", msg_id);

        // msg_id = esp_mqtt_client_subscribe(client, "/topic/qos1", 1);
        // ESP_LOGI(MQTT_TAG, "sent subscribe successful, msg_id=%d", msg_id);

        // msg_id = esp_mqtt_client_unsubscribe(client, "/topic/qos1");
        // ESP_LOGI(MQTT_TAG, "sent unsubscribe successful, msg_id=%d", msg_id);
        break;
    case MQTT_EVENT_DISCONNECTED: // 客户端断开连接
        ESP_LOGI(MQTT_TAG, "MQTT_EVENT_DISCONNECTED");
        break;

    case MQTT_EVENT_SUBSCRIBED: // 主题订阅成功
        ESP_LOGI(MQTT_TAG, "MQTT_EVENT_SUBSCRIBED, msg_id=%d", event->msg_id);
        msg_id = esp_mqtt_client_publish(client, "/topic/qos0", "data", 0, 0, 0);
        ESP_LOGI(MQTT_TAG, "sent publish successful, msg_id=%d", msg_id);
        break;
    case MQTT_EVENT_UNSUBSCRIBED: // 取消订阅
        ESP_LOGI(MQTT_TAG, "MQTT_EVENT_UNSUBSCRIBED, msg_id=%d", event->msg_id);
        break;
    case MQTT_EVENT_PUBLISHED: //  主题发布成功
        ESP_LOGI(MQTT_TAG, "MQTT_EVENT_PUBLISHED, msg_id=%d", event->msg_id);
        break;
    case MQTT_EVENT_DATA: // 已收到订阅的主题消息
        ESP_LOGI(MQTT_TAG, "MQTT_EVENT_DATA");
        printf("TOPIC=%.*s\r\n", event->topic_len, event->topic);
        printf("DATA=%.*s\r\n", event->data_len, event->data);
        break;
    case MQTT_EVENT_ERROR: // 客户端遇到错误
        ESP_LOGI(MQTT_TAG, "MQTT_EVENT_ERROR");
        if (event->error_handle->error_type == MQTT_ERROR_TYPE_TCP_TRANSPORT)
        {
            log_error_if_nonzero("reported from esp-tls", event->error_handle->esp_tls_last_esp_err);
            log_error_if_nonzero("reported from tls stack", event->error_handle->esp_tls_stack_err);
            log_error_if_nonzero("captured as transport's socket errno", event->error_handle->esp_transport_sock_errno);
            ESP_LOGI(MQTT_TAG, "Last errno string (%s)", strerror(event->error_handle->esp_transport_sock_errno));
        }
        break;
    default:
        ESP_LOGI(MQTT_TAG, "Other event id:%d", event->event_id);
        break;
    }
}

esp_mqtt_client_handle_t mqtt_app_start(void)
{
    esp_mqtt_client_config_t mqtt_cfg = {
        // See: https://www.jianshu.com/p/fdddc39510c1
        // .host = CONFIG_MQTT_BROKER_URL,
        .uri = CONFIG_MQTT_BROKER_URL,
        .port = CONFIG_MQTT_BROKER_PORT,
        .username = CONFIG_MQTT_CLIENT_USERNAME,
        .password = CONFIG_MQTT_CLIENT_PASSEORD,
        .lwt_topic = CONFIG_MQTT_CLIENT_TOPIC,
        .lwt_qos = CONFIG_MQTT_CLIENT_QOS,
    };

    esp_mqtt_client_handle_t client = esp_mqtt_client_init(&mqtt_cfg);
    /* The last argument may be used to pass data to the event handler, in this example mqtt_event_handler */
    esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, mqtt_event_handler, NULL);
    esp_mqtt_client_start(client);
    return client;
}
int mqtt_publish_message(esp_mqtt_client_handle_t client,const char *mesage)
{
    int msg_id=esp_mqtt_client_publish(

        client,                   // esp_mqtt_client_handle_t client,
        CONFIG_MQTT_CLIENT_TOPIC, // const char *topic,
        mesage,                   // const char *data,
        strlen(mesage),           // int len,
        CONFIG_MQTT_CLIENT_QOS,   // int qos,
        0                         // int retain
    );
    // vTaskDelay(2000 / portTICK_PERIOD_MS);
    return msg_id;
}
