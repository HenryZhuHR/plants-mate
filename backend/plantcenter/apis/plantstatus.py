import os
import datetime
import sys
import yaml
import json
import logging

from typing import List, Union

from threading import Thread

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

sys.path.append(settings.BASE_DIR)
from utils.error.error_code import ErrorResponse, ReturnHttpResponse

from ..models import PlantStatus

from .date_time_utils import CHECK_DATETIME

from django.views.decorators.csrf import csrf_exempt




logger = logging.getLogger('console')


@csrf_exempt
def plantstatus(request: WSGIRequest):
    if request.method == 'POST':
        # =============================================
        #   Check data (json)
        # =============================================
        try:
            request_json_data = json.loads(request.body)
        except:
            return ErrorResponse.Data.ErrorType(type(request.body))

        # =============================================
        #   Check Parameter
        # =============================================
        # if device exist
        if 'device' not in request_json_data:
            return ErrorResponse.Parameter.Missing("device")

        date_list = None
        if 'date' in request_json_data:
            date_list: List[str] = request_json_data['date']
            if len(date_list) not in [0, 1, 2]:
                return ErrorResponse.Parameter.Error("Too many items in <date>, expected 1 or 2.")
            for data in date_list:
                if not CHECK_DATETIME.is_valid_date(data):
                    return ErrorResponse.Parameter.Invalid(f"Invalid date format in <{data}>")

        time_list = None
        if 'time' in request_json_data:
            time_list: List[str] = request_json_data['time']
            if len(time_list) not in [0, 1, 2]:
                return ErrorResponse.Parameter.Error("Too many items in <time>, expected 1 or 2.")
            for data in time_list:
                if not CHECK_DATETIME.is_valid_time(data):
                    return ErrorResponse.Parameter.Invalid(f"Invalid time format in <{data}>")

        # =============================================
        #   Query filter
        # =============================================
        plants_status_all = PlantStatus.objects.all()

        plantstatus = plants_status_all.filter(device=request_json_data['device'])

        if isinstance(date_list, list):
            if len(date_list) == 1:
                plantstatus = plants_status_all.filter(date=datetime.date(*[int(d) for d in date_list[0].split('-')]))
            elif len(date_list) == 2:
                date_list_0 = [int(d) for d in date_list[0].split('-')]
                date_list_1 = [int(d) for d in date_list[1].split('-')]
                plantstatus = plants_status_all.filter(
                    date__range=[datetime.date(*date_list_0), datetime.date(*date_list_1)]
                )

        if isinstance(time_list, list):
            if len(time_list) == 1:
                plantstatus = plants_status_all.filter(time=datetime.time(*[int(d) for d in time_list[0].split('-')]))
            elif len(time_list) == 2:
                time_intlist_0 = [int(d) for d in time_list[0].split(':')]
                time_intlist_1 = [int(d) for d in time_list[1].split(':')]
                time_0 = time_intlist_0[0] * 10000 + time_intlist_0[1] * 100 + time_intlist_0[2]
                time_1 = time_intlist_1[0] * 10000 + time_intlist_1[1] * 100 + time_intlist_1[2]
                if time_0 >= time_1:
                    return ErrorResponse.Parameter.Invalid(f"Time {time_list[0]} must before {time_list[1]}")
                plantstatus = plants_status_all.filter(
                    time__range=[datetime.time(*time_intlist_0),
                                 datetime.time(*time_intlist_1)]
                )

        # return HttpResponse(json.dumps({}), content_type="application/json")

        # plantstatus=PlantStatus.objects.filter(device=request_json_data['device'])

        #
        data_list: List[dict] = []
        for status in plantstatus:
            data_json = {
                "date": status.date.strftime('%Y-%m-%d'),
                "time": status.time.strftime('%H:%M:%S'),
                "light": status.light,
                "temperature": status.temperature,
                "humidity": status.humidity,
            }
            # print(status.id,status.date,status.time,status.light,status.temperature,status.humidity)
            data_list.append(data_json)                  # sda
        return HttpResponse(
            json.dumps({'Response': {
                "device": request_json_data['device'],
                "data": data_list
            }}),
            content_type="application/json"
        )
    else:
        return HttpResponse('It is not a POST request!!!')# yapf:disable
