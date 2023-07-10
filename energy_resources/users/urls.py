from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ChangePasswordAPIView, RegisterAPIView, UserIdentityAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('status/', UserIdentityAPIView.as_view(), name='user_status'),
    path('register/', RegisterAPIView.as_view(), name='sign_up'),
]
