from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status
from .services import create_new_post

from .models import Post
from .serializer import PostSerializer

# Create your views here.

@api_view(['GET'])
def list_posts(request):

    try:
        posts = Post.objects.all()

        serializer = PostSerializer(posts,many=True)

        return Response({'posts':serializer.data},status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'posts':f'{e}'},status=status.HTTP_204_NO_CONTENT)

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
    
    
    
