from django.contrib import admin
from .models import Gist,Upvote,Downvote,GistComment,Category

admin.site.register(Gist)
admin.site.register(Upvote)
admin.site.register(Downvote)
admin.site.register(GistComment)
admin.site.register(Category)
