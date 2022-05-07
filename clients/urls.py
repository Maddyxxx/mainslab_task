from django.urls import path

from . import views

urlpatterns = [
    path('', views.GetClientInfoView.as_view()),
]
