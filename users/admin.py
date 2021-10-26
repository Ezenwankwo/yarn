from django.contrib import admin

from .models import Blogger, FollowRelation

class BloggerAdmin(admin.ModelAdmin):
    ...


class FollowRelationAdmin(admin.ModelAdmin):
    ...


admin.site.register(Blogger, BloggerAdmin)
admin.site.register(FollowRelation, FollowRelationAdmin)
