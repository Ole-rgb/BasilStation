from django.shortcuts import render
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
    #TODO what if id doesnt exist?
    waterings = Watered.objects.get(pk=watering_id) 
    serilizer = WateredSerializer(waterings, many=False)
    
    return Response(serilizer.data)
