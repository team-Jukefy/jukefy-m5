from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("users/", ),
    path("users/<int:pk>/", ),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
