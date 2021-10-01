from app.views import LikeHandleView
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def index(request):
    return render(request, 'index.html', {})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/<int:id>', LikeHandleView.as_view()),
    path('', index)

]
