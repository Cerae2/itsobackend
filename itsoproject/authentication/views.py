from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login upon successful registration
    template_name = 'registration/register.html'  # Template for user registration form
