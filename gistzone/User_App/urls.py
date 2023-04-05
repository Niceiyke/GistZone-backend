from django.urls import path
from . import views 

urlpatterns = [

    path('register/',views.register_user,name='create-user'),
    path('login/',views.login_user,name='login-user')

]