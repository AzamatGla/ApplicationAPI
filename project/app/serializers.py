from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'user', 'api_key')
        read_only_fields = ('api_key',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

