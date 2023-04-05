from rest_framework import serializers
from User_App.serializer import USerSerializer
from .models import UserProfile,TopicTag,SkillTag


class TopicTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicTag
        fields = '__all__'

class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = '__all__'

class ProfileSerilizer(serializers.ModelSerializer):
    user=USerSerializer(read_only=True)
    profile_pic = serializers.SerializerMethodField(read_only=True)
    interests = TopicTagSerializer(many=True, read_only=True)
    skills = SkillTagSerializer(many=True, read_only=True)

    class Meta:
        models=UserProfile
        fields ='__all__'
    def get_profile_pic(self, obj):
        try:
            pic = obj.profile_pic.url
        except:
            pic = None
        return pic