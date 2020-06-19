from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from api.models import Assignment, GradedAssignment
from api.serializers import AssignmentSerializer, GradedAssignmentSerializer


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


class GradedAssignmentListView(generics.ListAPIView):
    serializer_class = GradedAssignmentSerializer

    def get_queryset(self):
        queryset = GradedAssignment.objects.all()
        username = self.request.query_params.get('username', None)
        print('username >> ', username)

        if username is not None:
            queryset = queryset.filter(student__username=username)

        print('queryset >> ', queryset)
        return queryset


class GradedAssignmentCreateView(generics.CreateAPIView):
    serializer_class = GradedAssignmentSerializer
    queryset = GradedAssignment.objects.all()

    def post(self, request):
        print('request.data >> ', request.data)
        serializer = GradedAssignmentSerializer(data=request.data)

        if serializer.is_valid():
            graded_assignment = serializer.create(request)
            if graded_assignment:
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
