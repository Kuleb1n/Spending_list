from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Spending_list.apps.users.models import User
from Spending_list.apps.users.forms import RegisterUserForm


class LoginUserView(LoginView):
    template_name = 'user/login.html'

    def get_redirect_url(self):
        return reverse_lazy('main-page')


class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'user/login.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_message = 'You have successfully registered!'
