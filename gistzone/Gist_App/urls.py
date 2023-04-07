from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.list__latest_gist,name='list-gist')

]