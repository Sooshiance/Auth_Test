from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import User 



class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = User
        fields = ("id", "phone", "email")


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['phone', 'email', 'password']
        
    def create(self, **validated_data):
        return super(self, validated_data).create()


class LoginUserSerializer(serializers.Serializer):
    phone    = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
