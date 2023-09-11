from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
from .models import User, FriendshipRequest


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    """
    Нет ограничений на доступ, то есть права и аутентификация не требуются.
    Если же не указать два декоратора, то будет требовать аутентификацию и права по умолчанию.
    """
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()
    else:
        message = 'error'

    return JsonResponse({
        'message': message
    })


@api_view(['POST'])
def send_friendship_request(request, pk):
    print('send_friendship_request ', pk)
    user = User.objects.get(pk=pk)
    friendship_request = FriendshipRequest(created_for=user, created_by=request.user)
    return JsonResponse({
        'message': 'friendship request created successfully'
    })

