from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment, UserActionLog
from .decorators import log_user_action
from django.core.mail import send_mail
from django.shortcuts import render
from djangoProject import settings
from .forms import BlogPostForm

def is_moderator(user):
    return user.groups.filter(name='Moderator').exists() or user.is_staff

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
    post = get_object_or_404(BlogPost, pk=post_id)
    is_moderator = request.user.groups.filter(name='Moderator').exists()
    is_admin = request.user.groups.filter(name='Admin').exists()
    is_subscriber = request.user.groups.filter(name='Subscriber').exists()

    context = {
        'post': post,
        'is_moderator': is_moderator,
        'is_admin': is_admin,
        'is_subscriber': is_subscriber,
    }
    return render(request, 'post.html', context)

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
def user_action_log(request):
    logs = UserActionLog.objects.all().order_by('-timestamp')
    return render(request, 'user_action_log.html', {'logs': logs})

@login_required
@log_user_action('Like post')
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if not post.likes.filter(id=request.user.id).exists():
        post.likes.add(request.user)
    return redirect('specific-blog', post_id=post_id)

@login_required
@log_user_action('Dislike post')
def dislike_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    return redirect('specific-blog', post_id=post_id)

@login_required
@log_user_action('Comment post')
def comment_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(BlogPost, id=post_id)
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(
                blog_post=post,
                author=request.user,
                text=comment_text
            )
        return redirect('specific-blog', post_id=post_id)

@login_required
@log_user_action('Delete comment')
def delete_any_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('specific-blog', post_id=comment.blog_post.id)

@login_required
@log_user_action('Delete own comment')
def delete_own_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
    return redirect('specific-blog', post_id=comment.blog_post.id)

@login_required
@log_user_action('Delete post')
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.user.has_perm('BlogWebApp.delete_post'):
        post.delete()
    return redirect('blog_list')

@login_required
@log_user_action('Create post')
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user.username
            blog_post.save()
            return redirect('specific-blog', post_id=blog_post.id)
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

