from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import GradedAssignmentListView, GradedAssignmentCreateView

router = DefaultRouter()
urlpatterns = [
    path('', GradedAssignmentListView.as_view()),
    path('create/', GradedAssignmentCreateView.as_view()),
]
