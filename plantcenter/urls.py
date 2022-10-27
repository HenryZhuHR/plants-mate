from django.urls import path

from . import views
from . import apis

urlpatterns = [
    path('', views.index, name='index'),
    path('plantstatus', apis.plantstatus, name='plantstatus'),
]