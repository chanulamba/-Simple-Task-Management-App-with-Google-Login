# task_management/urls.py

from django.contrib import admin
from django.urls import path, include
from tasks.views import home  # Importing the home view from tasks/views.py

urlpatterns = [
    path('', home, name='home'),  # Root URL points to home view
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Google OAuth
    path('tasks/', include('tasks.urls')),  # Task management app
]
