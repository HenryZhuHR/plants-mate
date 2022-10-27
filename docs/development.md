
# 开发文档
- [开发文档](#开发文档)
  - [初始化](#初始化)
    - [创建项目](#创建项目)
    - [创建应用](#创建应用)
  - [启动](#启动)
  - [数据库相关](#数据库相关)
    - [数据库迁移](#数据库迁移)


## 初始化
### 创建项目
```shell
django-admin startproject PlantsMate
cd PlantsMate
```
### 创建应用

```shell
python3 manage.py startapp <app>
```

## 启动
```shell
python3 manage.py runserver
```

## 数据库相关

从 MQTT 接受到的数据格式为
```json
{
    "device": 746, // 设备 ID，基于Mac 地址
    "date": 20221026, // 日期
    "time": 190316, // 时间
    // 数据组
    "data": {
        "light": 99.97, // 光照程度
        "temperature": 30.02, // 温度
        "humidity": 52 // 湿度
    }
}
```



数据格式

| **名称** | **字段**    | **类型** | **说明**         |
| -------- | ----------- | -------- | ---------------- |
| 设备id   | device      | int      | (primary)        |
| 日期     | date        | date     |                  |
| 时间     | time        | time     |                  |
| 光照强度 | light       | float    | 光照强度(0~100%) |
| 温度     | temperature | float    |                  |
| 湿度     | humidity    | float    |                  |

设备id编号采用设备MAC地址后 3 个字节构成的整型数字。

例如某设备的完整MAC地址为 `84:F7:03:39:9F:C8` ，采用 `39:9F:C8` 所构成的 `int` 类型(通常为4字节)的数字作为编号。十六进制 `39`:`9F`:`C8` 分别对应十进制 `57`:`159`:`200`，按字节位置由高到低移位相加
```c
746 = (57 << (sizeof(byte) * 2)) + (159 << (sizeof(byte))) + 200;
```
就可以得到唯一的编号 `746`

> MAC 地址由 6 个字节组成。前 3 个字节表示厂商识别码，后 3 个字节表示厂商内识别码。因此采用后 3 字节进行设备表示



| 设备编号 | 设备Mac地址       |   
| -------- | ----------------- | 
| 746 | 84:F7:03:39:9F:C8 |   


### 数据库迁移

```shell
python3 manage.py makemigrations <app_name> # 激活数据表
python3 manage.py migrate   # 创建表结构
```





## 接口设计

### 请求

