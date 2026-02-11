from django.contrib import admin
from django.urls import path, include 
from django.views.generic import RedirectView  # <--- ADD THIS LINE
from tasks.views import dashboard, analytics_view
from rest_framework.routers import DefaultRouter 
from tasks.views import TaskViewSet , dashboard , create_task
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('task/new/', create_task, name='task_create'),
    path('analytics/', analytics_view, name='analytics'),
    # This makes the main link (/) go straight to the dashboard
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),
    path('api/', include(router.urls)),
    # Endpoints for Login and Refreshing Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]