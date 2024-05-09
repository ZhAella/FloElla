from django.contrib import admin
from . import models

admin.site.register(models.MenstrualDayStatus)
admin.site.register(models.SymptomName)
admin.site.register(models.UserSymptom)
admin.site.register(models.Reminder)
