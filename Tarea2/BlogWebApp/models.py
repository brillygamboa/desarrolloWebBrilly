from datetime import date
from django.db import models
from django.contrib.auth.models import User
from djangoProject import settings

class Message(models.Model):
    personName = models.CharField(max_length=50)
    personEmail = models.CharField(max_length=50)
    message = models.TextField()

    def is_valid(self):
        pass
    # TO DO: check if it is necessary

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    thumbnail_url = models.URLField()
    preview_text = models.TextField()
    text = models.TextField(default="")
    readingTimeInMinutes = models.IntegerField()
    publicationDate = models.DateField(default=date.today)
    author = models.CharField(max_length=50, default=settings.DEFAULT_BLOG_AUTHOR)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

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
