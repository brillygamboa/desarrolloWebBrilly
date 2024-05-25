from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, HttpResponse

from BlogWebApp.models import Message
from djangoProject import settings


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
