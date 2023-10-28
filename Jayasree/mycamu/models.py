from django.db import models
from django.contrib import admin
class Football (models.Model):
    playerid=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    goals=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('playerid','name','goals','age','email')