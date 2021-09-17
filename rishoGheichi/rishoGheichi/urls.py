import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static
from django.core.cache import cache

def index(request):
    cache.set("name", "ashkan", 50)
    context = {"title": "صفحه اصلی", "name" : "ashkan", "age": 19,"role": "customer"}
    return render(request, 'index.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home_page'),
    path('course/', include("course.urls")),
    path('account/', include("users.urls")),
    path('resume/', include("resume.urls")),
    path('exam/', include("exam.urls")),
    path('order/', include("order.urls")),
    path('__debug__/', include(debug_toolbar.urls)),
]


# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
