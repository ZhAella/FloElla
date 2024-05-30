from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('token/', views.JwtPairAPIView.as_view(), name='token_obtain_pair'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('user_update/', views.UserUpdateAPIView.as_view(), name='user_update'),

]
