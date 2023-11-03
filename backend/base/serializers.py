from rest_framework import serializers

from .models import User, Job, Application

class UserSerializer(serializers.ModelSerializer):
    """This serializer describes the User"""
    class Meta:
        model = User
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    """This serializer describes the Job"""
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    """"This serializer describes the Application"""
    class Meta:
        model = Application
        fields = '__all__'