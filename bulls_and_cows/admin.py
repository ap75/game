from django.contrib import admin

from .models import Game, Try


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass

@admin.register(Try)
class TryAdmin(admin.ModelAdmin):
    pass
