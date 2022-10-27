string(ASCII 27 Esc)
set(ColourReset "${Esc}[m")
set(BoldRed     "${Esc}[1;31m")
set(BoldGreen   "${Esc}[1;32m")
set(BoldYellow  "${Esc}[1;33m")
set(BoldMagenta "${Esc}[1;35m")
set(BoldCyan    "${Esc}[1;36m")
set(BoldWhite   "${Esc}[1;37m")

# The following lines of boilerplate have to be in your project's
# CMakeLists in this exact order for cmake to work correctly
cmake_minimum_required(VERSION 3.5)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)

project(plants_mate_esp)

message("${BoldCyan}Configuration Summary:${ColourReset}")
message("  ${BoldCyan}   Plateform: ${BoldGreen}${CMAKE_SYSTEM_NAME} ${CMAKE_SYSTEM_VERSION}${ColourReset}")
message("  ${BoldCyan}     C flags: ${BoldGreen}${CMAKE_C_FLAGS}${ColourReset}")
message("  ${BoldCyan}   C++ flags: ${BoldGreen}${CMAKE_CXX_FLAGS}${ColourReset}")
message("  ${BoldCyan}    idf path: ${BoldGreen}$ENV{IDF_PATH}${ColourReset}")



# idf_build_set_property(COMPILE_OPTIONS "-Wno-error" APPEND)

