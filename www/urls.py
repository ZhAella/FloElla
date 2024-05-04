from django.urls import path
from . import views

urlpatterns = [
    path('calendar/<int:year>/<int:month>/<int:day>/', views.MenstrualStatusDayAPIView.as_view(), name='get_status_for_day'),
    path('calendar/<int:year>/<int:month>/', views.MenstrualStatusMonthAPIView.as_view(), name='get_status_for_month'),
    path('calendar/<int:year>/', views.MenstrualStatusYearAPIView.as_view(), name='get_status_for_year'),
    path('symptoms/', views.SymptomListAPIView.as_view(), name='symptoms')
]
