from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework  import status

from .models import UserProfile
from .serializer import ProfileSerilizer

@api_view(['GET'])
def list_profiles(request):
    pass

