from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api


urlpatterns = [
    path('signup/', api.signup, name='signup'),
    path('me/', api.me, name='me'),
    path('login/', api.CustomTokenObtainPairView.as_view(), name='token-obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('friends/<uuid:pk>/', api.friends, name='friends'),
    path('friends/<uuid:pk>/request/', api.send_friendship_request, name='send_friendship_request'),
    path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),

    path('check_email/', api.CheckEmailExistsView.as_view(), name='check_email'),
    # path('check_inn/', api.CheckInnExistsView.as_view(), name='check_inn'),
    path('check_credentials/', api.CheckCredentialsView.as_view(), name='check_credentials'),
]
