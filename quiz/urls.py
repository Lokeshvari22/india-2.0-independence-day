from django.urls import path

from . import views


app_name = "quiz"


urlpatterns = [

    path(
        "",
        views.quiz,
        name="quiz"
    ),

    path(
        "result/",
        views.result,
        name="result"
    ),

    path(
        "restart/",
        views.restart,
        name="restart"
    ),

]