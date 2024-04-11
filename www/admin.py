from django.contrib import admin
from . import models

admin.site.register(models.MenstrualCycle)
admin.site.register(models.Status)
admin.site.register(models.Symptom)
admin.site.register(models.Reminder)
