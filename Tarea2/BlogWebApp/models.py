from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

class Message(models.Model):
    personName = models.CharField(max_length=50)
    personEmail = models.CharField(max_length=50)
    message = models.TextField()

    def is_valid(self):
        pass

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    thumbnail_url = models.URLField()
    preview_text = models.TextField()
    text = models.TextField(default="")
    readingTimeInMinutes = models.IntegerField()
    publicationDate = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.blog_post.title}'

class Category(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.action} at {self.timestamp}'

def create_roles_and_permissions():
    admin_group, created = Group.objects.get_or_create(name='Admin')
    moderator_group, created = Group.objects.get_or_create(name='Moderator')
    subscriber_group, created = Group.objects.get_or_create(name='Subscriber')

    # Admin permissions
    admin_permissions = Permission.objects.all()
    admin_group.permissions.set(admin_permissions)

    # Moderator permissions
    content_type = ContentType.objects.get_for_model(Comment)
    moderator_permissions = Permission.objects.filter(content_type=content_type)
    moderator_group.permissions.set(moderator_permissions)

    # Subscriber permissions
    subscriber_permissions = Permission.objects.filter(content_type=content_type, codename__in=['add_comment', 'delete_comment'])
    subscriber_group.permissions.set(subscriber_permissions)
