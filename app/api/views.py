from django.shortcuts import render
from rest_framework import viewsets

from api.models import Assignment
from api.serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
