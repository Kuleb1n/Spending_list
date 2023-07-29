from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from Spending_list.apps.users.models import User
from Spending_list.apps.users.forms import RegisterUserForm, EmailConfirmation


class LoginUserView(LoginView):
    template_name = 'user/login.html'

    def get_redirect_url(self):
        return reverse_lazy('main-page')

    def form_valid(self, form):
        if form.get_user().is_active:
            return super(LoginUserView, self).form_valid(form)


class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'user/login.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_message = 'You have successfully registered!\n' \
                      'Confirm the email address for authorization!'


class EmailConfirmationView(TemplateView):
    template_name = 'user/email_confirmation.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=kwargs['email'])
        link = kwargs['link']
        email_confirmation = EmailConfirmation.objects.filter(user=user, link=link)
        if email_confirmation.exists() and not email_confirmation.first().is_expired():
            user.is_active = True
            user.save()
            return super(EmailConfirmationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('main-page'))
