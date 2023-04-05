from rest_framework import serializers
from .models import Post,Upvote,Downvote
from User_App.serializer import USerSerializer



class UpvoteSerializer(serializers.ModelSerializer):
    upvoter = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model=Upvote
        fields=['upvoter']

    def get_upvoter(self,obj):

        return obj.upvoter.username

class DownvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Downvote
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):
    author = USerSerializer(read_only=True)
    upvotes =UpvoteSerializer(read_only=True,many=True)
    downvotes =UpvoteSerializer(read_only=True,many=True)


    class Meta:
        model=Post
        fields =['id','content','created','modified','author','upvotes','downvotes']