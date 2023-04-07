import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


User =get_user_model()

# A topic tag is added to by the user so they can content on their feed with the 
# related tags that
# They have selected
class TopicTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


# Skills are added by teh user to indicate topics they are proficient in
class SkillTag(models.Model):
    name = models.CharField(primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(blank=True, null=True, default='default.png')
    bio = models.TextField(null=True)
    followers = models.ManyToManyField(User, related_name='user_followers', blank=True)
    following = models.ManyToManyField(User, related_name='user_following', blank=True)
    skills = models.ManyToManyField(SkillTag, related_name='personal_skills', blank=True)
    muted = models.ManyToManyField(User, related_name='muted_users', blank=True)
    blocked = models.ManyToManyField(User, related_name='blocked_users', blank=True)
    interests = models.ManyToManyField(TopicTag, related_name='topic_interests', blank=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    """
    profile = UserProfile.objects.first()
    profile.followers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    """

    def __str__(self):
        return str(self.user.username)
    

@receiver(post_save,sender=User)
def ProfileCreate(sender,instance,created,*args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('profile created')