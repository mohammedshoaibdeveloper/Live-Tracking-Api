from django.urls import path,include
from livetracking.views import *





urlpatterns = [

    path('User_Signup',User_Signup.as_view()),
    path('Login',Login.as_view()),




]