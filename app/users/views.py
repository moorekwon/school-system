from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets

from users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
