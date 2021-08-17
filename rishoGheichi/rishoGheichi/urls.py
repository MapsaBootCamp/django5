from django.contrib import admin
from django.urls import path
from django.shortcuts import render


def index(request):
    context = {"name": "ashkan", "age": 19}
    return render(request, 'index.html', context)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home_page')
]
