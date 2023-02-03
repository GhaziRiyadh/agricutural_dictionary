from rest_framework import routers
from django.urls import path, include
from user.views import index, word

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('index/', index, name='index'),
    path('word/', word, name='word')
] + router.urls
