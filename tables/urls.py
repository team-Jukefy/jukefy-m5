from django.urls import path

from . import views

urlpatterns = [
    path("tables/", views.TableView.as_view()),
    path("tables/<int:pk>/", views.TableDetailView.as_view()),
    # path("tables/<int:pk>/orders", ),
    # path(
    #     "tables/<int:pk>/orders/<int:order_id>",
    # ),
    # path(
    #     "tables/<int:pk>/close",
    # ),
    # path(
    #     "tables/<int:pk>/music",
    # ),
]
