from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
# from post import api
#
# router = routers.DefaultRouter()
# router.register('posts', api.post_list)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('account.urls')),
    path('api/posts/', include('post.urls')),
    path('api/search/', include('search.urls')),
]
