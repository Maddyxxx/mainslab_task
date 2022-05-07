from django.urls import path

from . import views

urlpatterns = [
    path('load_client_org', views.load_client_org),
    path('load_bills', views.load_bills),

]