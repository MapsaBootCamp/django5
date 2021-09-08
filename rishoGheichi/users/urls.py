from django.urls import path

from .views import signup, login_view, logout_view, RegisterView, faghat_khodia, activate

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', signup, name='register'),
    path('activate/<str:uidb64>/<str:token>', activate, name='activate'),
    path('logout/', logout_view, name='logout'),
    path('private/', faghat_khodia, name='private'),
    path('register-class/', RegisterView.as_view(), name='register_class'),

]