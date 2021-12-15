from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from jobs.models import Job
from django.urls import reverse_lazy
from .forms import JobForm


class JobView(ListView):
    model = Job
    template_name = 'jobs.html'
    ordering = ['-id']


class JobsDetailedView(DetailView):
    model = Job
    template_name = 'jobs_detailed.html'


class AddJobsView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs_add.html'


class UpdateJobsView(UpdateView):
    model = Job
    # form_class = JobForm
    template_name = 'jobs_edit.html'
    fields = ('company_name', 'title', 'job_type', 'location', 'description', 'post_until', 'is_active', 'apply_link')


class DeleteJobsView(DeleteView):
    model = Job
    template_name = 'jobs_delete.html'
    success_url = reverse_lazy('jobs')
