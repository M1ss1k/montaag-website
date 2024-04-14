from django.urls import path
from . import views
app_name = "logistics"
urlpatterns = [
    path("", views.index, name="home"),
    path("tariffs", views.tariffs, name="tariffs"),
    path("contact-us", views.contact, name="contact"),
    path("order", views.create_order, name="create-order"),
]