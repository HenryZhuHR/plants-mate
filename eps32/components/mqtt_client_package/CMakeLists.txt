idf_component_register(
    SRCS "src/mqtt_client_package.c"
    INCLUDE_DIRS "include"
    REQUIRES nvs_flash lwip mqtt
)
