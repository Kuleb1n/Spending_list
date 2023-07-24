from django.contrib.auth.forms import UserCreationForm

from Spending_list.apps.users.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
