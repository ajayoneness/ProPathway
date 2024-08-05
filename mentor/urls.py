from django.urls import path
from . import views

urlpatterns = [

    path('', views.mentor, name="mentor"),
]


