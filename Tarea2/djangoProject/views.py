from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def resume(request):
    return render(request, 'resume.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')
