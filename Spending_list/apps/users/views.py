from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class LoginUserView(LoginView):
    template_name = 'user/login.html'

    def get_redirect_url(self):
        return reverse_lazy('main-page')
