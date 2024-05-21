from django.urls import path
from .views import MenstrualDayStatusAPIView

urlpatterns = [
    path('menstrual_status/', MenstrualDayStatusAPIView.as_view(), name='menstrual_status_list'),
    path('menstrual_status/<int:pk>/', MenstrualDayStatusAPIView.as_view(), name='menstrual_status_detail'),
]
