from rest_framework import serializers
from .models import Task

class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'