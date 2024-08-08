from django.urls import path
from . import views

urlpatterns = [

    path('', views.mentor, name="mentor"),
    path('mentor_list_api/', views.mentor_list, name="mentorlistapi"),
]


