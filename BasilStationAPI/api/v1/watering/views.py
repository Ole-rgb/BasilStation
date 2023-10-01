from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from base.models import Watered
from .serializers import WateredSerializer

# Create your views here.

#get all waterings
@api_view(['GET'])
def get_all_waterings(request):
    if request.GET.get('limit'):
        limit = int(request.GET.get('limit'))
        waterings = Watered.objects.order_by('-id')[:limit]
    else:
        waterings = Watered.objects.all()    
    
    serilizer = WateredSerializer(waterings, many=True)
    return Response(serilizer.data)

#get the last three waterings
@api_view(['GET'])
def get_watering(request, watering_id):
    try:
        waterings = Watered.objects.get(pk=watering_id) 
        serilizer = WateredSerializer(waterings, many=False)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Watering with id: {} doesnt exist".format(watering_id), )

    return Response(serilizer.data)
