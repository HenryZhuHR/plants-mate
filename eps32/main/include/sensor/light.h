#ifndef LIGHT_H
#define LIGHT_H
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_spi_flash.h"

#include "lwip/timeouts.h"

#include "driver/gpio.h"
#include "driver/adc.h"
#include "esp_adc_cal.h"

#define DEFAULT_VREF  1100 // Use adc2_vref_to_gpio() to obtain a better estimate
#define NO_OF_SAMPLES 64   // Multisampling

static esp_adc_cal_characteristics_t* adc_chars;
static const adc_channel_t            channel = ADC_CHANNEL_0; // GPIO34 if ADC1, GPIO14 if ADC2
static const adc_bits_width_t         width   = ADC_WIDTH_BIT_12;
static const adc_atten_t              atten   = ADC_ATTEN_DB_0;
static const adc_unit_t               unit    = ADC_UNIT_1;static float const MAX_VOLTAGE = 4096.;
// static uint32_t                       adc_reading = 0; // 光敏电阻读取数值
// static uint32_t                       voltage     = 0; // 光敏电阻电压


void  app_init_adc();
float light_get_light();
#endif