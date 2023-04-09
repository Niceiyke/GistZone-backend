from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Gist
from .serializer import GistSerializer

@api_view(["Get"])
def list__latest_gist(request):
    
    try:
        gist =Gist.objects.all()[:10]
        

        serializer = GistSerializer(gist,many=True)

        return Response({"Gist":serializer.data},status=status.HTTP_200_OK)
    
    except Exception as e:

        return Response({"error":f'{e}'},status=status.HTTP_400_BAD_REQUEST)
