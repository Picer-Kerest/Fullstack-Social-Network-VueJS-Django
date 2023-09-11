from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api


urlpatterns = [
    path('signup/', api.signup, name='signup'),
    path('me/', api.me, name='me'),
    path('login/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('friends/request/<uuid:pk>/', api.send_friendship_request, name='send_friendship_request'),
]
