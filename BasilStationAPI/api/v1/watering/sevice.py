from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response


from base.models import Watered
from .serializers import WateredSerializer


def handle_get_watering(request):
    if request.GET.get('limit'):
        limit = int(request.GET.get('limit'))
        waterings = Watered.objects.order_by('-id')[:limit]
    else:
        waterings = Watered.objects.all()    
    
    serilizer = WateredSerializer(waterings, many=True)
    return Response(serilizer.data, status=status.HTTP_200_OK)


def handle_get_watering_by_id(watering_id):
    try:
        waterings = Watered.objects.get(pk=watering_id) 
        serilizer = WateredSerializer(waterings, many=False)
    except ObjectDoesNotExist:
        return Response(data={"details":"watering with id {} doesnt exist".format(watering_id)}, status=status.HTTP_404_NOT_FOUND )
    
    return Response(serilizer.data, status=status.HTTP_200_OK)


def handle_post_watering(request):
    serializer = WateredSerializer(data=request.data)
    if serializer.is_valid():
        # GPIO
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(data={"details":"doesnt satisfy the data format"}, status=status.HTTP_400_BAD_REQUEST)
