import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from .services import create_new_post


from .models import Post
from .serializer import PostSerializer
from Profile_App.models import UserProfile

# Create your views here.

@api_view(['GET'])
def list_posts(request):
    user=request.user
    post=Post.objects.select_related('author').all()

    if user.is_banned:
        return Response({'posts':[]},status=status.HTTP_200_OK)



    try:
        profile =UserProfile.objects.prefetch_related('user','following').get(user=user)
        following =profile.following.all()
        muted =profile.muted.all()
        blocked =profile.blocked.all()
        

   #retriving all user following 
     
        user_following=[user for user in following]

    #retriving all user following 
     
        muted_users=[user for user in muted]

        blocked_users=[user for user in blocked]

        print(blocked_users)

        final_user_following= [user for user in user_following if user not in (muted_users or blocked_users)]
        
       

    # retriving all user following post 

        following_posts=post.filter(author__in=final_user_following)


     # retriving Top 5 post with highest Post Rank
        Top_Post = post.filter(post_rank__gte=1).exclude(author__in= muted_users).exclude(author__in= blocked_users).order_by('post_rank')[0:5]

    # retriving Top 5 post From High Ranking Gisters

        Post_From_Top_Gisters =post.filter(author__rank__gt=0).exclude(author__in= muted_users).exclude(author__in= blocked_users).order_by('created')[:5]
  

        user_feed = following_posts | Post_From_Top_Gisters | Top_Post 

        user_feed=(list(user_feed))

        print(len(user_feed))
        random.shuffle(user_feed)
        
        serializer =PostSerializer(user_feed, many=True)
     

        return Response({'posts':serializer.data},status=status.HTTP_200_OK)

    except Exception as e:
         return Response({'posts':str(e)},status=status.HTTP_200_OK)
       

@api_view(['GET'])
def get_post(request,pk):
    user= request.user
    
    if user.is_banned:
        return Response({'posts':[]},status=status.HTTP_200_OK)

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
    
    
    
