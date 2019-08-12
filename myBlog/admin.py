from django.contrib import admin

from myBlog.models import *


# Register your models here.
class articleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'thumbnail', 'date_publish', 'category', 'click_count')

    list_display_links = ('title', 'desc', 'thumbnail', 'click_count', 'date_publish', 'category')
    fieldsets = ((None, {'fields': ('title', 'desc', 'thumbnail', 'category', 'tag', 'content')}),)
    filter_horizontal = ('tag',)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, articleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Slide)
