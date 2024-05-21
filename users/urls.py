from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.GirlUserCreateAPIView.as_view(), name='user_register'),
]