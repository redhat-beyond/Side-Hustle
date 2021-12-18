from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from jobs.models import Job
from django.urls import reverse_lazy
from .forms import JobForm
from django.shortcuts import redirect
from django.db.models import Q


class JobView(ListView):
    model = Job
    template_name = 'jobs.html'
    ordering = ['-id']

    def dispatch(self, *args, **kwargs):
        # Check if user is authenticated
        if not self.request.user.is_authenticated:
            # Redirect them to the home page if not
            return redirect('home')

        # Render the template if they are
        return super(JobView, self).dispatch(*args, **kwargs)


class JobsDetailedView(DetailView):
    model = Job
    template_name = 'jobs_detailed.html'

    def dispatch(self, *args, **kwargs):
        # Check if user is authenticated
        if not self.request.user.is_authenticated:
            # Redirect them to the home page if not
            return redirect('home')

        # Render the template if they are
        return super(JobsDetailedView, self).dispatch(*args, **kwargs)


class AddJobsView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs_add.html'

    def dispatch(self, *args, **kwargs):
        # Check if user is authenticated
        if not self.request.user.is_authenticated:
            # Redirect them to the home page if not
            return redirect('home')

        if not self.request.user.role == 'HR':
            # Redirect them to the home page if not
            return redirect('jobs')

        # Render the template if they are
        return super(AddJobsView, self).dispatch(*args, **kwargs)


class UpdateJobsView(UpdateView):
    model = Job
    # form_class = JobForm
    template_name = 'jobs_edit.html'
    fields = ('company_name', 'title', 'job_type', 'location', 'description', 'post_until', 'is_active', 'apply_link')

    def dispatch(self, *args, **kwargs):
        # Check if user is authenticated
        if not self.request.user.is_authenticated:
            # Redirect them to the home page if not
            return redirect('home')

        if not self.request.user.role == 'HR':
            # Redirect them to the home page if not
            return redirect('jobs')

        # Render the template if they are
        return super(UpdateJobsView, self).dispatch(*args, **kwargs)


class DeleteJobsView(DeleteView):
    model = Job
    template_name = 'jobs_delete.html'
    success_url = reverse_lazy('jobs')

    def dispatch(self, *args, **kwargs):
        # Check if user is authenticated
        if not self.request.user.is_authenticated:
            # Redirect them to the home page if not
            return redirect('home')

        if not self.request.user.role == 'HR':
            # Redirect them to the home page if not
            return redirect('jobs')

        # Render the template if they are
        return super(DeleteJobsView, self).dispatch(*args, **kwargs)


class SearchResultsView(ListView):
    model = Job
    template_name = 'jobs_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Job.objects.filter(Q(title__icontains=query))
        return object_list
