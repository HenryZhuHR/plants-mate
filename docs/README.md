
# 开发文档
- [开发文档](#开发文档)
  - [初始化](#初始化)
    - [创建项目](#创建项目)
    - [创建应用](#创建应用)
  - [启动](#启动)
  - [数据库相关](#数据库相关)
    - [数据库迁移](#数据库迁移)
  - [接口文档](#接口文档)
    - [请求](#请求)


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

后台管理 `/admin`

## 数据库相关
[数据库](./data/database.md)

### 数据库迁移

```shell
python3 manage.py makemigrations <app_name> # 激活数据表
python3 manage.py migrate   # 创建表结构
```





## 接口文档

- [植物状态获取](./apis/plantcenter/plantstatus.md)

### 请求

```
POST / HTTP/1.1
url: /plantcenter/plantstatus
Content-Type: application/json
```

