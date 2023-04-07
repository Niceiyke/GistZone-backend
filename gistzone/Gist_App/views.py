from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Gist
from .serializer import GistSerializer

@api_view(["Get"])
def list__latest_gist(request):
    
    try:
        gist =Gist.objects.all().order_by('-created')[:10]
        

        serializer = GistSerializer(gist,many=True)

        return Response({"Gist":serializer.data},status=status.HTTP_200_OK)
    
    except Exception as e:

        return Response({"error":f'{e}'},status=status.HTTP_400_BAD_REQUEST)


@api_view(["Get"])
def list__top_gist(request):
    
    try:
        gist =Gist.objects.all().order_by('-gist_rank')[:10]
        

        serializer = GistSerializer(gist,many=True)

        return Response({"Gist":serializer.data},status=status.HTTP_200_OK)
    
    except Exception as e:

        return Response({"error":f'{e}'},status=status.HTTP_400_BAD_REQUEST)