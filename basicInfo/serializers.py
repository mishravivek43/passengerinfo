from  rest_framework import serializers
from basicInfo.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Passenger
        fields=['id', 'name','lastname','points']
