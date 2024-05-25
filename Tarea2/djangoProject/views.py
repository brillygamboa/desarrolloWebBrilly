from django.shortcuts import render, HttpResponse, get_object_or_404

from BlogWebApp.models import BlogPost


def index(request):
    return render(request, 'index.html')


def resume(request):
    return render(request, 'resume.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def message_form(request):
    return render(request, 'send_message.html')


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def specific_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()
    categories = post.categories.all()
    return render(request, 'post.html', {'post' : post, 'comments': comments, 'categories': categories})

