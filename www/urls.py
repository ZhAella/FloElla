from django.urls import path
from . import views

urlpatterns = [
    path('calendar/<int:year>/<int:month>/<int:day>/', views.MenstrualStatusDayAPIView.as_view(), name='get_status_for_day'),
    path('calendar/', views.MenstrualStatusWeekAPIView.as_view(), name='get_status_for_week'),
    path('calendar/<int:year>/<int:week>/', views.MenstrualStatusWeekAPIView.as_view(), name='get_status_for_week'),
    path('calendar/<int:year>/<int:month>/', views.MenstrualStatusMonthAPIView.as_view(), name='get_status_for_month'),
    path('calendar/<int:year>/', views.MenstrualStatusYearAPIView.as_view(), name='get_status_for_year'),
    path('calendar/<int:year>/<int:month>/<int:day>/symptoms/', views.SymptomAPIView.as_view(), name='symptoms'),
    path('calendar/<int:year>/<int:month>/<int:day>/mark_start_day/', views.MarkMenstrualStartDayStatus.as_view(), name='mark_start_day'),
    path('calendar/<int:year>/<int:month>/<int:day>/mark_day/', views.MarkMenstrualDayStatus.as_view(), name='mark_menstrual_day'),
    path('calendar/<int:year>/<int:month>/<int:day>/mark_end_day/', views.MarkMenstrualEndDayStatus.as_view(), name='mark_end_day')
]
