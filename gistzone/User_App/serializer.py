from rest_framework import serializers
from django.contrib.auth import get_user_model


User =get_user_model()

class USerSerializer(serializers.ModelSerializer):
    full_name =serializers.SerializerMethodField(read_only =True)
    
    class Meta:
        model =User
        fields =['id','username','email','full_name']

    def get_full_name(self,obj):
        return obj.get_full_name()