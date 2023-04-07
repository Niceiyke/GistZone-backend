import uuid
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Upvote(models.Model):
    id =models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    upvoter =models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_upvoters')
    post =models.ForeignKey('Post',on_delete=models.CASCADE, related_name='upvotes')
    created =models.DateTimeField(auto_now_add=True)

class Downvote(models.Model):
    id =models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    downvoter =models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_downvoters')
    post =models.ForeignKey('Post',on_delete=models.CASCADE,related_name='downvotes')
    created =models.DateTimeField(auto_now_add=True)

class PostComment(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,db_index=True)
    content =models.CharField(max_length=1000,)
    post=models.ForeignKey('Post',on_delete=models.CASCADE,related_name='comments')
    created=models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)


class Post(models.Model):
    id =models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    author =models.ForeignKey(User,on_delete=models.CASCADE,db_index=True)
    content = models.CharField(max_length=1000,)
    post_rank =models.PositiveIntegerField(default=0)
    created =models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


