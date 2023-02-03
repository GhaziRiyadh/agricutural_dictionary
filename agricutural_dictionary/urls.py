from django.contrib import admin
from django.urls import path, include
from user.urls import urlpatterns as user_routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(user_routers)),
]
