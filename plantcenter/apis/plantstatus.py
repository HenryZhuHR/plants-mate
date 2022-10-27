from threading import Thread
from ..models import PlantStatus
from .error_code import ERROR_CODES
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
import os
import yaml
import json
import logging

logger = logging.getLogger('console')


def plantstatus(request: WSGIRequest):
    if request.method == 'POST':
        

        return HttpResponse(json.dumps({'Response': {}}), content_type="application/json")

    else:
        return HttpResponse('It is not a POST request!!!')
