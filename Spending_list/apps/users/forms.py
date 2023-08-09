import datetime
import uuid
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from Spending_list.apps.users.models import User, EmailConfirmation


class UserAuthenticationForm(AuthenticationForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password
            )
            if len(User.objects.filter(email=email)) == 1 and not self.user_cache:
                user = User.objects.get(email=email)
                if user.is_active in (False,):
                    self.confirm_login_allowed(self.user_cache)
                else:
                    raise self.get_invalid_login_error()

            else:
                self.get_invalid_login_error()

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        raise ValidationError(
            self.error_messages["inactive"],
            code="inactive",
        )


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=True)
        link = uuid.uuid4()
        expiration_of_time = now() + datetime.timedelta(days=2)
        email_confirmation = EmailConfirmation.objects.create(
            link=link,
            user=user,
            expiration_of_time=expiration_of_time)
        email_confirmation.sending_confirmation_by_email()
        return user
