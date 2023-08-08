from datetime import date, datetime
from django.db import models

from Spending_list.apps.spending_operations.managers import GoalManager, GoalType


class Category(models.Model):
    name = models.CharField(
        "Название категории",
        max_length=64,
        unique=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Operation(models.Model):
    name = models.TextField(
        "Наименование операции"
    )
    description = models.TextField(
        "Описание операции",
        blank=True,
        null=True,
    )
    cost = models.FloatField(
        "Стоимость"
    )
    operation_at = models.DateTimeField(
        "Дата операции",
        default=datetime.now,
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="operations",
        verbose_name="Категория операции",
    )

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"

    def __str__(self):
        return f"At-{self.operation_at}-{self.name}"


class Goal(models.Model):
    """Модель цели траты или пополнения"""

    name = models.CharField(
        "Название цели",
        max_length=255,
    )
    description = models.TextField(
        "Описание",
        blank=True,
        null=True,
    )
    goal_type = models.CharField(
        "Тип операций цели",
        choices=GoalType.choices,
        default=GoalType.SPENDING,
        max_length=32,
    )
    start_date = models.DateField(
        "Дата начала цели",
        default=date.today,
    )
    finish_date = models.DateField(
        "Дата окончания цели",
        blank=True,
        null=True, )
    value = models.FloatField(
        "Значение цели"
    )

    objects = GoalManager()

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"
