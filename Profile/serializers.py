from django.contrib.auth.models import User
from rest_framework import serializers
from .models import user, Restaurant, FuelStation, Hotel


content = [
    {
        'error': 0,
        'response': 'success'
    }
]
error = [
    {
        'error': 1,
        'response': 'fail'
    }
]


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('name', 'password', 'email')


class restaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('name','url','address','city','latitude','longitude','zipcode','average_cost_for_two','currency','menu_url','aggregate_rating','rating_text','votes','cuisines')



class locationSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('name','latitude','longitude')


class FuelStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStation
        fields = ('Name','CompanyName','Address','City','State')

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ('Name','HotelUrl','Address')


# class HotelviewerSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Hotel
#         fields = ('Name')




class LoginSerializer(serializers.ModelSerializer):
    def validate(self, data):
        x = user.objects.filter(email=data['email'])
        if x:
            ls = user.objects.get(email=data['email'])
            if ls.password == data['password']:
                return data
        else:
            raise serializers.ValidationError(error)

    class Meta:
        model = user
        fields = ('email', 'password')