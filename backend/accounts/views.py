import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializer, StaffSerializer

from .models import Staff


@api_view(["POST"])
def register(request):
    data = request.data

    user = SignUpSerializer(data=data)

    if user.is_valid():
        if not Staff.objects.filter(email=data["email"]).exists():
            user = Staff.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=make_password(data["password"]),
            )
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

    return Response(user.errors)
