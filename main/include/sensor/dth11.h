#ifndef DTH11_H
#define DTH11_H
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_spi_flash.h"

#include "lwip/timeouts.h"

#include "driver/gpio.h"
#include "driver/adc.h"
#include "esp_adc_cal.h"

#define DHT11_PIN     GPIO_NUM_1 // https://zhuanlan.zhihu.com/p/136157998

typedef unsigned char byte;
typedef struct
{
    float temperature;
    float humidity;
} DTH11_DATA;




byte       dth11_read_byte();
DTH11_DATA dth11_get();
#endif