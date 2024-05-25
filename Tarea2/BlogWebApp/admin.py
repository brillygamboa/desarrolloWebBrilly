from django.contrib import admin

# Register your models here.
from .models import Message, Comment, Category
from .models import BlogPost

admin.site.register(Message)

admin.site.register(BlogPost)

admin.site.register(Comment)

admin.site.register(Category)
