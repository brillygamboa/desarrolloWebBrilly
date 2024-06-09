from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from BlogWebApp.models import BlogPost, Comment
from django.core.mail import send_mail
from djangoProject import settings

def index(request):
    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')

def about(request):
    return render(request, 'about.html')

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def specific_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()
    return render(request, 'post.html', {'post': post, 'comments': comments})

def message_form(request):
    return render(request, 'send_message.html')

def message_view(request):
    if request.method == 'POST':
        form = Message(request.POST)
        if form.is_valid():
            message = Message(
                email=form.cleaned_data['email'],
                name=form.cleaned_data['name'],
                message=form.cleaned_data['message']
            )
            message.save()

            send_mail(
                subject='[BlogWebApp] Here is a new message from {}'.format(form.cleaned_data['name']),
                message=form.cleaned_data['message'],
                from_email=message.personEmail,
                recipient_list=[settings.DEFAULT_BLOGGER_EMAIL],
                fail_silently=False,
            )

            return redirect('success')

    return render(request, 'message_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('specific-blog', post_id=post_id)

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        Comment.objects.create(blog_post=post, author=request.user, text=comment_text)
    return redirect('specific-blog', post_id=post_id)
