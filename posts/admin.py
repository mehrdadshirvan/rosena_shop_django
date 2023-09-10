from django.contrib import admin
from .models import Posts


# Register your models here.
# Register your models here.

# class PostsAdmin(admin.ModelAdmin):
#     readonly_fields = ("slug",)
#     list_filter = ("name")
#     list_display = ('id',"name")
    # prepopulated_fields = {"slug": ("name",)}


admin.site.register(Posts)