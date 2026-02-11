import os
import django
import random
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from tasks.models import Task
from django.contrib.auth.models import User

def seed_db():
    # Get the user you created earlier
    user = User.objects.filter(is_superuser=True).first()
    if not user:
        print("Please create a superuser first!")
        return

    task_titles = [
        "Cloud Infrastructure Audit", "Q1 Financial Reporting", 
        "Security Patch Deployment", "User Experience Research",
        "API Documentation Update", "Database Optimization",
        "Frontend Refactoring", "Client Presentation Prep",
        "Marketing Automation Setup", "Legacy Code Cleanup"
    ]

    print(f"Seeding data for user: {user.username}...")
    
    for i in range(20):
        Task.objects.create(
            title=f"{random.choice(task_titles)} #{i+1}",
            owner=user,
            priority=random.randint(1, 5),
            is_completed=random.choice([True, False]),
            # Logic: Assign some tasks to the past and some to the future
            due_date=timezone.now() + timedelta(days=random.randint(-5, 10))
        )
    print("Success! 20 enterprise tasks added.")

if __name__ == "__main__":
    seed_db()