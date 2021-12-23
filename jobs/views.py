from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from jobs.models import Job
from django.urls import reverse_lazy
from .forms import JobForm
from django.shortcuts import redirect


class JobView(ListView):
    model = Job
    template_name = 'jobs.html'
    ordering = ['-id']

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super(JobView, self).dispatch(*args, **kwargs)


class JobsDetailedView(DetailView):
    model = Job
    template_name = 'jobs_detailed.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        return super(JobsDetailedView, self).dispatch(*args, **kwargs)


class AddJobsView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs_add.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        if not self.request.user.role == 'HR':
            return redirect('jobs')

        return super(AddJobsView, self).dispatch(*args, **kwargs)


class UpdateJobsView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs_edit.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        if not self.request.user.role == 'HR':
            return redirect('jobs')

        return super(UpdateJobsView, self).dispatch(*args, **kwargs)


class DeleteJobsView(DeleteView):
    model = Job
    template_name = 'jobs_delete.html'
    success_url = reverse_lazy('jobs')

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')

        if not self.request.user.role == 'HR':
            return redirect('jobs')

        return super(DeleteJobsView, self).dispatch(*args, **kwargs)
