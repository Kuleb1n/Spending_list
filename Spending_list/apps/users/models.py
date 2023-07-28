from Spending_list import settings
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy


class User(AbstractUser):
    email = models.EmailField(
        gettext_lazy("Email address"),
        unique=True,
        validators=[validators.validate_email],
        error_messages={
            "unique": gettext_lazy("A user with that email already exists."),
        },
    )
    is_active = models.BooleanField(
        gettext_lazy("Active"),
        default=False,
        help_text=gettext_lazy(
            "Indicates whether this user should be considered active."
            "(Is the account verified?)"
        ),
    )
    image = models.ImageField('Image URL', blank=True, upload_to='users/%Y/%m/%d/')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.email}'


class EmailConfirmation(models.Model):
    """ A class for confirming a user account """

    link = models.UUIDField('Link', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='For the user')
    date = models.DateTimeField(auto_now_add=True)
    expiration_of_time = models.DateTimeField()

    def __str__(self):
        return f'Email confirmation for {self.user.email}'

    def sending_confirmation_by_email(self):
        """ Sending an email to the user's email to confirm the account """

        link = reverse('email-confirmation', kwargs={'email': self.user.email, 'link': self.link})
        full_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Account confirmation for {self.user.email}'
        message = f'To confirm your account {self.user.email}, follow the link {full_link}'

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=self.user.email,
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration_of_time else False
