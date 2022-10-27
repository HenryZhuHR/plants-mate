

## 开发环境设备与设备烧录
[搭建 ESP32 硬件开发的软件环境](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/get-started/index.html)

[连接设备](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/get-started/index.html#get-started-connect)
```shell
ls -al /dev/cu.*
#  Ctrl-A + \ 退出
screen /dev/cu.Bluetooth-Incoming-Port 115200 
screen /dev/cu.usbserial-110 115200
```

[配置](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/get-started/index.html#get-started-configure)
```shell
get_idf # 激活环境
idf.py set-target esp32-c3 # 设置目标芯片
idf.py menuconfig   # 配置
```

[编译工程](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/get-started/index.html#get-started-build)
```shell
idf.py build
```

[烧录到设备](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/get-started/index.html#get-started-flash) 或者使用[监视器](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/get-started/index.html#get-started-build-monitor) 监视设备运行情况
```shell
idf.py \
    -p /dev/cu.usbserial-110 \
    -b 460800 \
    flash
idf.py -p /dev/cu.usbserial-110 monitor # Ctrl+] 退出
```


## 构建项目
[构建系统（CMake 版](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/api-guides/build-system.html#cmake)


[idf.py 工具](https://docs.espressif.com/projects/esp-idf/zh_CN/v4.4.2/esp32/api-guides/build-system.html#idf-py)


[C++开发](https://blog.csdn.net/m0_50064262/article/details/118695186)




