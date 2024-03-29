"""
Django settings for PlantsMate project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5&hjh@5seu#y^rjqg8++jsm^3mfa+8f0j3=fp+_w3=0ts8-$&&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',# CORS 放在新建的其他项目之前
    'plantcenter.apps.PlantcenterConfig',  # mqtt_manager: https://docs.djangoproject.com/zh-hans/4.1/intro/tutorial02/#activating-models
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # CORS 注意顺序，必须放在这儿
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # 关闭 CSRF 验证 https://www.jianshu.com/p/671deb51a968
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PlantsMate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PlantsMate.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'plants_mate',  # 连接的数据库
        'HOST': 'henryzhuhr.xyz',  # mysql的ip地址
        'PORT': 3306,  # mysql的端口
        'USER': 'plantsmate',  # mysql的用户名
        'PASSWORD': '20221018',  # mysql的密码
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propagate': False,
                }
            },
        },
    }
}

# Log
# https://docs.djangoproject.com/zh-hans/4.1/topics/logging/
# https://cloud.tencent.com/developer/article/1935322
LOG_PATH = os.path.join(BASE_DIR, 'log')
os.makedirs(LOG_PATH, exist_ok=True)

LOGGING = {
    'version': 1,  # version 值只能为1
    'disable_existing_loggers': False,

    # < 格式化 >
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s %(funcName)s %(module)s %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(module)s  %(message)s'
        }
    },

    # < 处理信息 >
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 若日志超过指定文件的大小，会再生成一个新的日志文件保存日志信息
            'maxBytes': 5 * 1024 * 1024,  # 指定文件大小 1M=1024kb 1kb=1024b
            'filename': '%s/debug.log' % LOG_PATH,
            'formatter': 'default'
        },
        'file_warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',  # 若日志超过指定文件的大小，会再生成一个新的日志文件保存日志信息
            'maxBytes': 5 * 1024 * 1024,  # 指定文件大小 1M=1024kb 1kb=1024b
            'filename': '%s/warning.log' % LOG_PATH,
            'formatter': 'default'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_debug','file_warning'],
            'level': 'DEBUG'
        },
    },
    'filters': {}
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 'en-us'

TIME_ZONE = 'Asia/Shanghai'  # 'UTC'
DATETIME_FORMAT = "Y-m-d H:i:s" # https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#date
DATE_FORMAT = "Y-m-d" 
TIME_FORMAT = "H:i:s"
USE_THOUSAND_SEPARATOR = True

USE_I18N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

SIMPLEUI_STATIC_OFFLINE = True # 离线模式 https://simpleui.72wo.com/docs/simpleui/QUICK.html#离线模式
STATIC_URL = 'static/'
STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "assets"),
 ]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PROJECT_CONFIG = BASE_DIR / 'configs/settings.yaml'



# Simple UI config  https://simpleui.72wo.com/docs/simpleui/
SIMPLEUI_STATIC_OFFLINE = True # 离线模式
SIMPLEUI_LOGO = 'https://s3.plumeta.com/i/2022/10/29/hhba5y.png'
# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_HOME_ACTION = False
SIMPLEUI_ANALYSIS = False

# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com' # 可用于嵌入其他链接，这里可以直接方便的嵌入报表链接
# SIMPLEUI_HOME_ICON = 'el el-icon-platform-eleme'
# ICON 支持element-ui和fontawesome  eg：fa fa-user





# 跨域配置
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
#允许所有的请求头
CORS_ALLOW_HEADERS = ('*')