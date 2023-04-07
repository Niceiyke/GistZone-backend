from django.contrib import admin
from .models import Gist,Upvote,Downvote,GistComment

admin.site.register(Gist)
admin.site.register(Upvote)
admin.site.register(Downvote)
admin.site.register(GistComment)
