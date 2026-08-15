from django.urls import path

from . import views


app_name = "history"


urlpatterns = [

    path(
        "",
        views.timeline,
        name="timeline"
    ),

    path(
        "<int:event_id>/",
        views.event_detail,
        name="event_detail"
    ),

]