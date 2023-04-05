from django.contrib.auth import authenticate


def Login(request):
    data=request.data
    email = data.get('email')
    password = data.get('password')
    return authenticate(email=email,password=password)
    
