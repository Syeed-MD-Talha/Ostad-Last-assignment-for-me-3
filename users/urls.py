from django.urls import path
from . import views

app_name = 'users'  # Add this line

urlpatterns = [
    path('profile/<int:id>',views.ProfileView.as_view(),name='profile'),
    path('register',views.sign_up.as_view(),name='register'),
    path('login',views.sign_in,name='login'),
    path('logout',views.sign_out,name='logout'),
    path('home',views.home,name='home'),
]
