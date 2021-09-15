from django.urls import path
from .views import home, post

urlpatterns = [
    path('',home,name="home"),
    path('post/',post,name="post"),
]