set(wifi_station_srcs "src/wifi_connect.c")

idf_component_register(
    SRCS "${wifi_station_srcs}"
    INCLUDE_DIRS "include"
    REQUIRES nvs_flash
    )