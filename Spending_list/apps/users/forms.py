import datetime
import uuid

from django.contrib.auth.forms import UserCreationForm
from django.utils.timezone import now

from Spending_list.apps.users.models import User, EmailConfirmation


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
