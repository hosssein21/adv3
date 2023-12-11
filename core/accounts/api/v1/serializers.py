from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

class RegistrationSerializer(serializers.ModelSerializer):
    
    password1=serializers.CharField(max_length=180,write_only=True)
    
    class Meta:
        model=User
        fields = ["email", "password","password1"]
        
    def validate(self, attrs):
        if attrs.get('password')!=attrs.get('password1'):
            return serializers.ValidationError("confirm password does not match password")
        try:
            validate_password(attrs.get('password'))
            
        except exceptions.ValidationError as e:
            return serializers.ValidationError(list(e.message))
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1', None)
        return User.objects.create_user(**validated_data)
    