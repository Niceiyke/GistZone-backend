from django.contrib.auth import authenticate
from .models import myUser

def Login(request):
    data=request.data
    email = data.get('email')
    password = data.get('password')
    return authenticate(email=email,password=password)
    
def Register(request):
    data =request.data
    return myUser.objects.create(email=data.get('email'),username=data.get('username'),first_name=data.get('first_name'),last_name=data.get('last_name'))