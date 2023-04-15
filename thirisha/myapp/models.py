from django.db import models
from django.contrib import admin
class student (models.Model):
    sid=models.CharField(max_length=28)
    name=models.CharField(max_length=30)
    regno=models.IntegerField()
    marks=models.IntegerField()
    email=models.EmailField()

class studentAdmin(admin.ModelAdmin):
    list_display=('sid','name','regno','marks','email')
