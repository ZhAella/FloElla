from django.urls import path
from . import views

urlpatterns = [
    path('get_or_update_day/', views.MenstrualDayStatusAPIView.as_view(), name='get_or_update_day'),
    path('get_days/', views.UserMenstrualDaysStatusAPIView.as_view(), name='get_days'),
    path('get_week/', views.UserMenstrualDaysWeekStatusAPIView.as_view(), name='get_week'),
    path('get_month/', views.UserMenstrualDaysMonthStatusAPIView.as_view(), name='get_month'),
    path('update_symptom/', views.UpdateSymptomAPIView.as_view(), name='update_symptom'),

]
