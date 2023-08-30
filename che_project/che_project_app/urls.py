from django.urls import path

from . import views  # Import your views from the same directory

app_name = "che_project_app"
urlpatterns = [
    # Car list page
    path("", views.car_list, name="car_list"),
    # Car detail page
    path("detail/car_id=<int:id>/", views.car_detail, name="detail"),
    # Chat page
    path("detail/<int:id>/chat/", views.chat, name="chat"),
    # Checkout page
    path("detail/car_id=<int:id>/checkout/", views.checkout, name="checkout"),
    # Success page
    path("detail/car_id=<int:id>/success/", views.success_page, name="success_page"),
    # Info update page
    path("info/update/", views.info_update, name="info_update"),
]
