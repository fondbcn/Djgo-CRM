from django.urls import path
from . import views

app_name="website"
urlpatterns = [
    path('',views.home,name="home"),
    path('logout/',views.logout_r,name="logout"),
    path('signup/',views.signup,name="signup"),
]
