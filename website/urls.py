from django.urls import path
from . import views

app_name="website"
urlpatterns = [
    path('',views.home,name="home"),
    path('logout/',views.logout_r,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('detail/<int:pk>/',views.detail,name="detail"),
    path('delete/<int:pk>/',views.delete,name="delete"),
    path('add_item/',views.add,name="add"),
    path('edit/<int:pk>/',views.edit,name="edit"),
]
