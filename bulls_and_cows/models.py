from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')
    number = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Гра"
        verbose_name_plural = "Гри"

    def __str__(self):
        return f"Game #{self.pk} for {self.user.username}"

    @property
    @admin.display(boolean=True)
    def is_finished(self):
        return self.tries.filter(bulls=4).exists()

    @property
    def tries_count(self):
        return self.tries.count()


class Try(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='tries')
    guess = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )
    bulls = models.PositiveIntegerField()
    cows = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Try {self.guess}"
