from django.urls import path

from . import views

app_name = "burningwheelrolls"

urlpatterns = [
    path("roll_dice/", views.roll_dice, name="roll_dice"),
    path("roll_luck/", views.roll_luck, name="roll_luck"),
    path("assess_difficulty/", views.assess_difficulty, name="assess_difficulty"),
]
