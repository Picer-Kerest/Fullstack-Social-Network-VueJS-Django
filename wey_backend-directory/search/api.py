from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from post.models import Post
from account.serializers import UserSerializer
from post.serializers import PostSerializer


@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']

    users = User.objects.filter(name__icontains=query)
    posts = Post.objects.filter(body__icontains=query)
    # icontains - содержит без учёта регистра
    users_serializer = UserSerializer(users, many=True)
    posts_serializer = PostSerializer(posts, many=True)
    return JsonResponse({
        'users': users_serializer.data,
        'posts': posts_serializer.data,
    }, safe=False)

