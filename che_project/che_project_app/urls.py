from django.urls import path

from . import views  # Import your views from the same directory

app_name = "che_project_app"
urlpatterns = [
    # car list page
    path("", views.car_list, name="car_list"),
    path("detail/<int:id>/", views.detail_view, name="detail"),
    # path("about/", views.about_view, name="about"),
    path("detail/<int:id>/chat/", views.chat, name="chat"),
    path("info/update/", views.info_update, name="info_update"),
]
