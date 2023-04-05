from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import USerSerializer
from .services import Login,Register

@api_view(['POST'])
def register_user(request):
    new_user =Register(request)
    serializer =USerSerializer(new_user)
    return Response({'user':serializer.data},status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    user=Login(request)
    if user is not None:
        serializer =USerSerializer(user)
        return Response({'Logged in':serializer.data},status=status.HTTP_202_ACCEPTED)  
    return Response({'Not Logged in':user},status=status.HTTP_202_ACCEPTED)





