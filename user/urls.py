from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from .views import *


urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
    path('api/token/', UserLoginAPIView.as_view(), name='login'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
