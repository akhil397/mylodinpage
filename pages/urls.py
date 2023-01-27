from django.urls import path
from pages import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('chage_password/',views.chagepass, name='chagepass')
]