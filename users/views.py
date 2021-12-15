from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
