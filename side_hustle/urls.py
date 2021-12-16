from django.contrib import admin
from django.contrib.auth.urls import path
from django.urls import include
from jobs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.JobView.as_view(), name="jobs"),
    path('jobs', views.JobView.as_view(), name="jobs"),
    path('jobs/<int:pk>', views.JobsDetailedView.as_view(), name="jobs_detailed"),
    path('jobs/add/', views.AddJobsView.as_view(), name="jobs_add"),
    path('jobs/edit/<int:pk>', views.UpdateJobsView.as_view(), name="jobs_edit"),
    path('jobs/delete/<int:pk>', views.DeleteJobsView.as_view(), name="jobs_delete"),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls'))
]
