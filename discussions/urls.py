from django.urls import path
from . import views

urlpatterns = [



    path('<slug:slug>/', views.Discussion, name='discussion'),

    # path('discussions/', views.discussions_list, name='discussions_list'),
    # path('discussion-replies/', views.discussion_reply_list, name='discussion_reply_list'),
   

]


