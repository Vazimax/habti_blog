from django.contrib import admin
from .models import Post

admin.site.register(Post)

admin.site.site_header = "Habti's Blog"
admin.site.site_title = "Habti's Blog"