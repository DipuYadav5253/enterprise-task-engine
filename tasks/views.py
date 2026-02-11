from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only the tasks owned by the current user
        return Task.objects.filter(owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically associate the task with the logged-in user
        serializer.save(owner=self.request.user)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def dashboard(request):
    # The "Analysis" Logic
    user_tasks = Task.objects.filter(owner=request.user)
    total = user_tasks.count()
    completed = user_tasks.filter(is_completed=True).count()
    
    # Calculate performance metric
    performance = (completed / total * 100) if total > 0 else 0
    
    return render(request, 'tasks/dashboard.html', {
        'tasks': user_tasks,
        'total': total,
        'performance': round(performance, 2),
        'pending': total - completed
    })