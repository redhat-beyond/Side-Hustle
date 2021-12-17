from django.contrib import admin
from django.contrib.auth.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('jobs/', include('jobs.urls')),
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='home'),
]
