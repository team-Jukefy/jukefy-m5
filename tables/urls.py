from django.urls import path

from orders import views as order_views

from . import views

urlpatterns = [
    path("tables/", views.TableView.as_view()),
    path("tables/<int:pk>/", views.TableDetailView.as_view()),
    path("tables/<int:pk>/orders/", views.TableOrderView.as_view()),
    path(
        "tables/<int:table_id>/orders/<int:pk>", order_views.OrderDetailView.as_view()
    ),
    path("tables/<int:pk>/close/", views.TableCloseView.as_view()),
    # path(
    #     "tables/<int:pk>/music",
    # ),
]
