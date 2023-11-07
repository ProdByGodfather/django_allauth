from django.urls import path
from main_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path("login/",views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]