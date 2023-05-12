import os
import yaml
import json
import logging

logger = logging.getLogger('console')

from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings

from .models import PlantStatus

from threading import Thread
from .mqtt_client_utils import start_mqtt

t_mqtt = Thread(target=start_mqtt, args=(settings.PROJECT_CONFIG, ))
# t_mqtt.start()


def index(request: WSGIRequest):
    return HttpResponse("Hello, world. You're at the plantcenter index.")



