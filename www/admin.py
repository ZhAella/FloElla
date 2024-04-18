from django.contrib import admin
from . import models

admin.site.register(models.MenstrualDayStatus)
admin.site.register(models.Symptom)
admin.site.register(models.Reminder)
