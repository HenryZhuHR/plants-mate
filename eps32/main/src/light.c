#include "sensor/light.h"

void app_init_adc()
{
    // https://blog.csdn.net/m0_50064262/article/details/118817032
    adc1_config_width(width);
    adc1_config_channel_atten(channel, atten);
    adc_chars                    = calloc(1, sizeof(esp_adc_cal_characteristics_t));
    esp_adc_cal_value_t val_type = esp_adc_cal_characterize(unit, atten, width, DEFAULT_VREF, adc_chars);
    if (val_type == ESP_ADC_CAL_VAL_EFUSE_TP)
    {
        printf("Characterized using Two Point Value\n");
    }
    else if (val_type == ESP_ADC_CAL_VAL_EFUSE_VREF)
    {
        printf("Characterized using eFuse Vref\n");
    }
    else
    {
        printf("Characterized using Default Vref\n");
    }
}

float light_get_light()
{
    uint32_t adc_reading = 0;
    for (int i = 0; i < NO_OF_SAMPLES; i++)
    {
        adc_reading += adc1_get_raw((adc1_channel_t)channel);
    }
    adc_reading /= NO_OF_SAMPLES;
    // voltage = esp_adc_cal_raw_to_voltage(adc_reading, adc_chars);
    return adc_reading / MAX_VOLTAGE;
}
