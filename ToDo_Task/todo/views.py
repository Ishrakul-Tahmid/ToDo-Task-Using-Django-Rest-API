from rest_framework import generics
from .models import Task
from .serializers import ToDoTaskSerializer

# List all Tasks (GET all)
class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoTaskSerializer


# Create a new Task (Insert)
class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoTaskSerializer

# Update an existing Task
class TaskUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoTaskSerializer
    lookup_field = 'pk'

# Delete a Task (RetrieveUpdateDestroy handles delete too)
class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoTaskSerializer
    lookup_field = 'pk'

# Retrieve a Task (GET)
class TaskRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = ToDoTaskSerializer
    lookup_field = 'pk'
