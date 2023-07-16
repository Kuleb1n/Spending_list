from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
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
