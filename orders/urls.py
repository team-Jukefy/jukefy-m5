from django.urls import path

from . import views

urlpatterns = [
    path("orders/", ),
    path("orders/<int:pk>/", ),
]
