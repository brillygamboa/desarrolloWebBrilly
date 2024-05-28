from django.shortcuts import render, HttpResponse, get_object_or_404
from BlogWebApp.models import BlogPost

## @package views
#  Este módulo contiene las vistas de la aplicación web.

## Vista para la página principal.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'index.html'.
def index(request):
    return render(request, 'index.html')

## Vista para la página de resumen.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'resume.html'.
def resume(request):
    return render(request, 'resume.html')

## Vista para la página "Sobre mí".
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'about.html'.
def about(request):
    return render(request, 'about.html')

## Vista para la página del blog.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'blog.html'.
def blog(request):
    return render(request, 'blog.html')

## Vista para la página del formulario de mensajes.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'send_message.html'.
def message_form(request):
    return render(request, 'send_message.html')

## Vista para la lista de publicaciones del blog.
#  Ordena las publicaciones por el parámetro dado en la URL.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'blog.html' con las publicaciones ordenadas.
def blog_list(request):
    order_by = request.GET.get('order_by')

    if order_by == 'likes':
        posts = BlogPost.objects.all().order_by('-likesCount')
    elif order_by == 'publication_date':
        posts = BlogPost.objects.all().order_by('-publicationDate')
    else:
        posts = BlogPost.objects.all()

    return render(request, 'blog.html', {'posts': posts})

## Vista para una publicación específica del blog.
#  Muestra la publicación junto con sus comentarios y categorías.
#  @param request La solicitud HTTP.
#  @param post_id El ID de la publicación.
#  @return Una respuesta HTTP que renderiza la plantilla 'post.html' con la publicación, comentarios y categorías.
def specific_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()
    categories = post.categories.all()
    return render(request, 'post.html', {'post' : post, 'comments': comments, 'categories': categories})
