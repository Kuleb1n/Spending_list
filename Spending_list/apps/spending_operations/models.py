from datetime import date, datetime
from django.db import models


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

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"

    def __str__(self):
        return f"At-{self.operation_at}-{self.name}"


class GoalType(models.TextChoices):
    """Тип цели"""

    SPENDING = "Трата"
    REFILL = "Пополнение"


class GoalManager(models.Manager):
    def goals(self):
        return self.filter(goal_type=GoalType.REFILL)

    def budgets(self):
        return self.filter(goal_type=GoalType.SPENDING)


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
