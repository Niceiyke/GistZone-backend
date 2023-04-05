from django.urls import path
from . import views 

urlpatterns = [

    path('create/',views.create_post,name='create-post'),
    path('',views.list_posts,name='list-posts'),
    path('<str:pk>/',views.get_post,name='post-detail'),
    path('<str:pk>/delete',views.delete_post,name='post-delete'),
    

]