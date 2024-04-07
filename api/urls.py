from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestAPIView.as_view(), name='testapi'),
    path('login/', views.LoginUserAPIView.as_view(), name='loginapi'),
    path('register/', views.RegisterAPIView.as_view(), name='registerapi'),
    path('profile/update/', views.ProfileUpdateAPIView.as_view(), name='profile-updateapi'),
    path('profile/image/', views.ProfileImageAPIView.as_view(), name='profile-imageapi'),
    path('logout/', views.LogoutUserAPIView.as_view(), name='logoutapi'),
    path('level/', views.LevelAPIView.as_view(), name='levelapi'),
    path('dashboard/', views.DashboardAPIView.as_view(), name='dashboardapi'),
    path('level/one/', views.LevelOneAPIView.as_view(), name='level-oneapi'),
    path('level/two/', views.LevelTwoAPIView.as_view(), name='level-twoapi'),
    path('level/three/', views.LevelThreeAPIView.as_view(), name='level-threeapi'),
    path('certification/', views.CertificationAPIView.as_view(), name='certificationapi'),
]
