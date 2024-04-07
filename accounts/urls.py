from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test,name="test"),
    path('',views.loginuser,name="main"),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('level-one/', views.level_one, name='level1'),
    path('level-two/', views.level_two, name='level2'),
    path('level-three/', views.level_three, name='level3'),
    path('certification-level/', views.certification, name='certification'),
    path('profile-update/', views.ProfileUpdate, name='profileupdate'),
    path('profile-image/', views.ProfileImage, name='profileimage'),
    path('pay/',views.Pay,name="rezpay"),

]


