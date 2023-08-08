from django.db import models


class GoalType(models.TextChoices):
    """Тип цели"""

    SPENDING = "Трата"
    REFILL = "Пополнение"


class GoalManager(models.Manager):
    def goals(self):
        return self.filter(goal_type=GoalType.REFILL)

    def budgets(self):
        return self.filter(goal_type=GoalType.SPENDING)
