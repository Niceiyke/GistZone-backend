
from rest_framework import serializers


from .models import Upvote,Downvote,Gist,GistComment
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

class CommentsSerializer(serializers.ModelSerializer):
    owner = USerSerializer(read_only=True)

    class Meta:
        model=GistComment
        fields='__all__'

class GistSerializer(serializers.ModelSerializer):
    owner = USerSerializer(read_only=True)
    upvotes =UpvoteSerializer(read_only=True,many=True)
    downvotes =UpvoteSerializer(read_only=True,many=True)
    comments =CommentsSerializer(read_only=True,many=True)



    class Meta:
        model=Gist
        fields =['id','title','content','created','gist_rank','modified','owner','upvotes','downvotes','comments']
