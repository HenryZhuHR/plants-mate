clear
rm -rf build
rm sdkconfig*
ls -al /dev/cu.*
# wait
. $PROGRAM_DIR/esp/esp-idf/export.sh
idf.py set-target esp32-c3 # 设置目标芯片
# idf.py menuconfig   # 配置

# idf.py \
#     -p /dev/cu.usbserial-2130 \
#     -b 460800 \
#     flash
idf.py -p /dev/cu.usbserial-2130 flash monitor