from django.contrib import admin
from .models import Post
from .models import Commits


admin.site.register(Post)
admin.site.register(Commits)
