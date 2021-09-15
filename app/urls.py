from django.urls import path
from .views import home, post, about_me

urlpatterns = [
    path('',home,name="home"),
    path('post/<str:id>/',post,name="post"),
    path('about_me/',about_me,name="about_me"),
]