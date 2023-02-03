from rest_framework import routers
from django.urls import path, include
from user.views import index

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('index/', index, name='index'),
] + router.urls
