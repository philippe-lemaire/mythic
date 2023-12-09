from django.urls import path

from . import views

app_name = "gmemulator"

urlpatterns = [
    path("fate-question", views.fate_question, name="fate_question"),
]
