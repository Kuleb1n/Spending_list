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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.email}'
