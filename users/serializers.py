from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from houses.models import House
from devices.models import Device
from .models import UserProfile

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, phone=phone)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name', 'location']

    def create(self, validated_data):
        user = self.context['request'].user
        return House.objects.create(user=user, **validated_data)

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'device_uid', 'api_key', 'house']
        read_only_fields = ['id', 'api_key']

    def validate_house(self, value):
        user = self.context['request'].user
        if value.user != user:
            raise serializers.ValidationError("This house does not belong to you.")
        return value




