from django.shortcuts import render

def index(request):
    """
    Render the index page.

    :param request: The HTTP request object.
    :return: Rendered HTML of the index page.
    """
    return render(request, 'index.html')

def resume(request):
    """
    Render the resume page.

    :param request: The HTTP request object.
    :return: Rendered HTML of the resume page.
    """
    return render(request, 'resume.html')

def about(request):
    """
    Render the about page.

    :param request: The HTTP request object.
    :return: Rendered HTML of the about page.
    """
    return render(request, 'about.html')

def blog(request):
    """
    Render the blog page.

    :param request: The HTTP request object.
    :return: Rendered HTML of the blog page.
    """
    return render(request, 'blog.html')
