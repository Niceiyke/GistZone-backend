from .models import Post
from .serializer import PostSerializer
from rest_framework.response import Response
from rest_framework  import status

def create_new_post(request):
        
    user =request.user
    data = request.data
    #Add Business Logic Here
    post=Post.objects.create(content=data.get('content'),author=user)
    serializer =PostSerializer(post,many=False)
    return serializer

            
        
