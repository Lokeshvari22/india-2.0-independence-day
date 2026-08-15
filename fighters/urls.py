from django.urls import path

from . import views


app_name = "fighters"


urlpatterns = [

    path(
        "",
        views.fighter_list,
        name="fighter_list"
    ),

    path(
        "<int:fighter_id>/",
        views.fighter_detail,
        name="fighter_detail"
    ),

    path(
        "random/",
        views.random_fighter,
        name="random_fighter"
    ),

]