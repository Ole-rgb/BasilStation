from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from base.models import Watered
from .serializers import WateredSerializer

from .sevice import handle_get_watering, handle_get_watering_by_id, handle_post_watering

import json
# Create your views here.


@api_view(['GET','POST'])
def watering(request):
    if request.method == 'GET':
        return handle_get_watering(request)
    elif request.method == 'POST':
        #TODO GPIO PUT 
        return handle_post_watering(request)


#get the last three waterings
@api_view(['GET'])
def watering_by_id(request, watering_id):
    return handle_get_watering_by_id(watering_id)


