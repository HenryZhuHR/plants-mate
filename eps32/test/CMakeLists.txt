

# The following lines of boilerplate have to be in your project's
# CMakeLists in this exact order for cmake to work correctly
cmake_minimum_required(VERSION 3.5)
project(test_cjson)

include_directories(.)
add_executable(main main.c cJSON.c cJSON.h)