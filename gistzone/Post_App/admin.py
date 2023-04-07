from django.contrib import admin
from .models import Post,Upvote,Downvote,PostComment

admin.site.register(Post)
admin.site.register(Upvote)
admin.site.register(Downvote)
admin.site.register(PostComment)
