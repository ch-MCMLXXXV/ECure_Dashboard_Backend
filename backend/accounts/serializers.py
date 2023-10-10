from .models import Staff
from django.contrib.auth import get_user_model
from rest_framework import serializers


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        user = get_user_model()
        model = Staff
        fields = ("id", "first_name", "last_name", "email", "password")

        extra_kwargs = {
            "first_name": {"required": True, "allow_blank": False},
            "last_name": {"required": True, "allow_blank": False},
            "email": {"required": True, "allow_blank": False},
            "password": {"required": True, "allow_blank": False, "min_length": 6},
        }


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        user = get_user_model()
        model = Staff
        fields = ("id", "first_name", "last_name", "email")
