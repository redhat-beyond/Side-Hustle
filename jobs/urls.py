from django.contrib.auth.urls import path
from . import views

urlpatterns = [
    path('', views.JobView.as_view(), name="jobs"),
    path('<int:pk>', views.JobsDetailedView.as_view(), name="jobs_detailed"),
    path('add/', views.AddJobsView.as_view(), name="jobs_add"),
    path('edit/<int:pk>', views.UpdateJobsView.as_view(), name="jobs_edit"),
    path('delete/<int:pk>', views.DeleteJobsView.as_view(), name="jobs_delete"),
    path('search', views.SearchResultsView.as_view(), name="jobs_search"),
]
