from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from .services import create_new_post
from itertools import chain

from .models import Post
from .serializer import PostSerializer
from Profile_App.models import UserProfile

# Create your views here.

@api_view(['GET'])
def list_posts(request):
    user=request.user
    post=Post.objects.select_related('author').all()

    try:
        profile =UserProfile.objects.select_related('user').get(user=user)
        following =profile.following.all()

   #retriving all user following id
        following_ids=[]
        for user in following:
            following_ids.append(user)

    # retriving all user following post through their id
        following_posts=[]
        Post_From_Top_Gisters =post.filter(author__rank__gt=0)
  
        Top_Post = post.filter(post_rank__gte=1)


        follo=post.filter(author_id__in=following_ids)
     
        
        for id in following_ids:
            post=post.filter(author=id)
            if post.count()>0:
                following_posts.append(post)


        

        matches = Post_From_Top_Gisters | Top_Post | follo
        print('ee',matches.count())

        matches.distinct()

        print('df',matches.count())

       

        
        feed_post= list(chain(following_posts, Top_Post, Post_From_Top_Gisters))
       

            

        return Response({'posts':'done'},status=status.HTTP_200_OK)

    except Exception as e:
         return Response({'posts':str(e)},status=status.HTTP_200_OK)
       

@api_view(['GET'])
def get_post(request,pk):

    try:
        post =Post.objects.get(id=pk)
        serializer =PostSerializer(post,many=False)
        return Response({'posts':serializer.data},status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'posts':f'{e}'},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['DELETE'])
def delete_post(request,pk):
    user =request.user
    
    post =Post.objects.select_related('author').get(id=pk)

    if post.author==user:
        post.delete()
        return Response({'post': f'{post.id} deleted'})
    
    else:return Response({'post':'you can not delete a post you did not create'})

@api_view(['POST'])
def create_post(request):
    response =create_new_post(request)
    return Response({'posts':response.data},status=status.HTTP_201_CREATED)
    
    
    
