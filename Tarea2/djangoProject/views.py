from django.shortcuts import render, HttpResponse, get_object_or_404
from BlogWebApp.models import BlogPost

## @package views
#  Este m�dulo contiene las vistas de la aplicaci�n web.

## Vista para la p�gina principal.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'index.html'.
def index(request):
    return render(request, 'index.html')

## Vista para la p�gina de resumen.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'resume.html'.
def resume(request):
    return render(request, 'resume.html')

## Vista para la p�gina "Sobre m�".
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'about.html'.
def about(request):
    return render(request, 'about.html')

## Vista para la p�gina del blog.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'blog.html'.
def blog(request):
    return render(request, 'blog.html')

## Vista para la p�gina del formulario de mensajes.
#  @param request La solicitud HTTP.
#  @return Una respuesta HTTP que renderiza la plantilla 'send_message.html'.
def message_form(request):
    return render(request, 'send_message.html')

## Vista para la lista de publicaciones del blog.
#  Ordena las publicaciones por el par�metro dado en la URL.
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

## Vista para una publicaci�n espec�fica del blog.
#  Muestra la publicaci�n junto con sus comentarios y categor�as.
#  @param request La solicitud HTTP.
#  @param post_id El ID de la publicaci�n.
#  @return Una respuesta HTTP que renderiza la plantilla 'post.html' con la publicaci�n, comentarios y categor�as.
def specific_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()
    categories = post.categories.all()
    return render(request, 'post.html', {'post' : post, 'comments': comments, 'categories': categories})
