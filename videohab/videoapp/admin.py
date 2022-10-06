from django.contrib import admin
from .models import Users, Clips, Comments, ClipsLikes, CommentsLikes, Subscribes, BlackLists

admin.site.register(Users)
admin.site.register(Subscribes)
admin.site.register(BlackLists)
admin.site.register(Clips)
admin.site.register(ClipsLikes)
admin.site.register(Comments)
admin.site.register(CommentsLikes)


