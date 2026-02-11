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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
from django.db.models import Q

from django.utils import timezone
from datetime import timedelta

@login_required
def dashboard(request):
    user_tasks = Task.objects.filter(owner=request.user)
    total = user_tasks.count()
    completed = user_tasks.filter(is_completed=True).count()
    pending = total - completed
    urgent = user_tasks.filter(priority__gte=4, is_completed=False).count()
    
    # --- AUTOMATED INSIGHTS LOGIC ---
    efficiency = (completed / total * 100) if total > 0 else 0
    
    # Logic 1: Determine System Health
    if urgent > 3:
        health_status = "CRITICAL"
        advice = "System overload. Immediate focus required on Level 4+ tasks to prevent bottleneck."
        color = "rose"
    elif pending > 10 and efficiency < 40:
        health_status = "WARNING"
        advice = "Backlog is growing faster than completion rate. Consider delegating low-priority items."
        color = "amber"
    else:
        health_status = "STABLE"
        advice = "Operations optimal. You are maintaining a healthy throughput."
        color = "emerald"

    # Logic 2: Smart Recommendation
    # Find the oldest high-priority task that isn't done
    top_task = user_tasks.filter(is_completed=False).order_by('-priority', 'due_date').first()

    context = {
        'tasks': user_tasks,
        'total': total,
        'pending': pending,
        'efficiency': round(efficiency, 1),
        'urgent': urgent,
        'health_status': health_status,
        'advice': advice,
        'health_color': color,
        'top_task': top_task
    }
    return render(request, 'tasks/dashboard.html', context)
    # 1. Fetch data specifically for the logged-in user


@login_required
def analytics_view(request):
    user_tasks = Task.objects.filter(owner=request.user)
    
    # Logic for the Charts
    total = user_tasks.count()
    completed = user_tasks.filter(is_completed=True).count()
    
    # Get counts for each priority level (1-5) for the bar chart
    priority_counts = [
        user_tasks.filter(priority=i).count() for i in range(1, 6)
    ]
    
    context = {
        'total': total,
        'completed': completed,
        'efficiency': round((completed/total)*100, 1) if total > 0 else 0,
        'priority_counts': priority_counts, # This goes to Chart.js
    }
    return render(request, 'tasks/analytics.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user  # Connect the task to YOU
            task.save()
            return redirect('dashboard')  # Go back to dashboard after saving
        else:
            # This will print errors in your terminal for debugging
            print(form.errors) 
    else:
        form = TaskForm()
        
    return render(request, 'tasks/task_form.html', {'form': form})