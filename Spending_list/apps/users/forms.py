import datetime
import uuid
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from Spending_list.apps.users.models import User, EmailConfirmation


def create_link_and_date():
    """A function that returns the code and the
    expiration date of the code for the email"""

    return uuid.uuid4(), now() + datetime.timedelta(days=2)


class UserAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login":
            "Please enter a correct email and password. Note that both "
            "fields may be case-sensitive.",
        "inactive": "This account is inactive."
                    "Go to your email address provided during registration and"
                    " confirm your account to log in (Check the spam folder).",
        "invalid_data": "The data entered in the form fields is incorrect.",
    }

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
                    user_email_confirmation = EmailConfirmation.objects.get(user_id=user.pk)
                    if now() > user_email_confirmation.expiration_of_time:
                        user_email_confirmation.link, user_email_confirmation.expiration_of_time = (
                            create_link_and_date())
                        user_email_confirmation.save()
                        user_email_confirmation.sending_confirmation_by_email()
                    self.confirm_login_allowed(self.user_cache)
                else:
                    raise self.get_invalid_login_error()

            elif not self.user_cache:
                raise ValidationError(
                    self.error_messages["invalid_data"],
                    code="invalid_data",
                )

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
        link, expiration_of_time = create_link_and_date()
        email_confirmation = EmailConfirmation.objects.create(
            link=link,
            user=user,
            expiration_of_time=expiration_of_time)
        email_confirmation.sending_confirmation_by_email()
        return user
