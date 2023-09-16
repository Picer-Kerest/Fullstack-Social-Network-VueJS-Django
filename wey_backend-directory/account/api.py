from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer


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

    new_user = {}

    if form.is_valid():
        form.save()
        new_user = User.objects.get(email=data.get('email'))
        new_user = UserSerializer(new_user)
        new_user = new_user.data
    else:
        """
        В Django эти правила пароля могут быть настроены в файле настроек проекта 
        (settings.py) с помощью переменных, таких как MINIMUMPASSWORDLENGTH 
        (минимальная длина пароля), COMMONPASSWORDS (список популярных паролей), 
        SIMILARITYTHRESHOLD (порог схожести с другой личной информацией) и другие. 
        Django автоматически проводит проверку пароля пользователя при создании аккаунта или 
        изменении пароля и отображает это сообщение, если пользователь 
        не соответствует указанным требованиям.
        """
        print('form: ', form)
        # Закинуть валидаторы
        #
        message = 'error'
    print('request.data: ', request.data)
    return JsonResponse({
        'message': message,
        'user': new_user
    })


@api_view(['GET'])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = request.data
    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests
    }, safe=False)


@api_view(['POST'])
def send_friendship_request(request, pk):
    user = User.objects.get(pk=pk)
    friendship_request = FriendshipRequest.objects.create(created_for=user, created_by=request.user)
    return JsonResponse({
        'message': 'friendship request created successfully'
    })

