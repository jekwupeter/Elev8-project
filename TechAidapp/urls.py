from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('sign', views.signin,name="signin"),
    path('login', views.login,name="login"),
    path('hospital', views.hospital,name="hospital"),
    path('base', views.base,name="base"),
]