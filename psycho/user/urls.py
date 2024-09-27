from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet

user = routers.DefaultRouter()
user.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(user.urls)),
    path('users/<int:pk>/', UserViewSet.as_view, name="users"),
]
