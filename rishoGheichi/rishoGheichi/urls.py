from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def index(request):
    context = {"title": "صفحه اصلی", "name" : "ashkan", "age": 19,"role": "customer"}
    return render(request, 'index.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home_page'),
    path('course/', include("course.urls")),

]
