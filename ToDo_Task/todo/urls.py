from django.urls import path
from .views import (
    TaskListAPIView,
    TaskCreateAPIView,
    TaskUpdateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    TaskRetrieveAPIView,
)

urlpatterns = [
    path('', TaskListAPIView.as_view(), name='task-list'),        
    path('create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-delete'),
    path('<int:pk>/get/', TaskRetrieveAPIView.as_view(), name='task-detail'),
]
