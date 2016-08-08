from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_native(self, obj):
        """Remove password field when serializing an object"""
        ret = super(UserSerializer, self).to_native(obj)
        del ret['password']
        return ret
