from rest_framework import serializers
from base.models import Watered

# objects to data that the response objects can understand

class WateredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watered
        fields = '__all__'