from django.urls import path

from . import views

urlpatterns = [
    path("menu/", ),
    path("menu/<int:pk>/", ),
]
