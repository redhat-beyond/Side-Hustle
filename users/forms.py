from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User  # this is the "YourCustomUser" that you imported at the top of the file
        fields = ('first_name', 'last_name', 'email', 'role', 'username', 'password1', 'password2')
