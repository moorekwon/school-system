from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import Assignment
from api.serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def create(self, request):
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
