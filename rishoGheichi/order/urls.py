from django.urls import path

from .views import course_add_to_cart
urlpatterns = [
    path('course-add-to-cart/<int:course_id>', course_add_to_cart, name='course_add_to_cart'),
]
