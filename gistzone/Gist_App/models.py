import uuid
from django.db import models
from django.contrib.auth import get_user_model



User=get_user_model()


class Upvote(models.Model):
    id =models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    upvoter =models.ForeignKey(User,on_delete=models.CASCADE,related_name='gist_upvoter')
    gist =models.ForeignKey('Gist',on_delete=models.CASCADE, related_name='upvotes')
    created =models.DateTimeField(auto_now_add=True)

class Downvote(models.Model):
    id =models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    downvoter =models.ForeignKey(User,on_delete=models.CASCADE,related_name='gist_downvoter')
    gist =models.ForeignKey('Gist',on_delete=models.CASCADE,related_name='downvotes')
    created =models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image=models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)
    gist =models.ForeignKey('Gist',related_name='images',blank=True,null=True,on_delete=models.CASCADE)
    created =models.DateTimeField(auto_now_add=True)

class GistComment(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,db_index=True)
    content =models.CharField(max_length=1000,)
    gist=models.ForeignKey('Gist',on_delete=models.CASCADE,related_name='comments')
    created=models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)



class Gist(models.Model):
    id =models.UUIDField(uuid.uuid4,unique=True, primary_key=True, editable=False)
    owner =models.ForeignKey(User,on_delete=models.CASCADE,db_index=True)
    title =models.CharField(max_length=500)
    content = models.CharField(max_length=1000,)
    gist_rank =models.PositiveIntegerField(default=0)
    created =models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def post_comments(self):
        return self.comments.filter(parent=self).order_by('created')

