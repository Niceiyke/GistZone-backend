from rest_framework import serializers
from User_App.models import myUser
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Q


User =get_user_model()

class USerSerializer(serializers.ModelSerializer):
    password =serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model =User
        fields =['id','username','email','first_name','last_name','password']

    
    def validate(self, attrs):
        email_exist = myUser.objects.filter(email=attrs["email"] ).exists()
        username_exist = myUser.objects.filter(username=attrs["username"]).exists()
        if email_exist:
            raise ValidationError("Email has already been taken")
        if username_exist:
            raise ValidationError("Username has already been taken")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password =validated_data.pop('password')
        user= super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    