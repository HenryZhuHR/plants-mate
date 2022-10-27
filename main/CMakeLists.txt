
file(GLOB srcs ./src/*.c)
list(APPEND srcs "main.c")

idf_component_register(
    SRCS "${srcs}"
    INCLUDE_DIRS "include"
    REQUIRES freertos spi_flash lwip json wifi_connect mqtt_client_package esp_adc_cal ssd1306
)

