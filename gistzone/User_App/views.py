from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import USerSerializer
from .services import Login

@api_view(['POST'])
def register_user(request):
    data= request.data
    serializer =USerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        
        response = {"message": "User Created Successfully", "data": serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    user=Login(request)
    if user is not None:
        serializer =USerSerializer(user)
        return Response({'Logged in':serializer.data},status=status.HTTP_202_ACCEPTED)  
    return Response({'Not Logged in':user},status=status.HTTP_202_ACCEPTED)





