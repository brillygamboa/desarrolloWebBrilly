"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
from BlogWebApp import views as blog_views
from .views import blog_list, specific_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", blog_views.index, name="index"),
    path("resume", blog_views.resume, name="resume"),
    path("about", blog_views.about, name="about"),
    path("send-message", blog_views.message_form, name="send-message"),
    path('blog/', blog_views.blog_list, name='blog_list'),
    path('blog/<int:post_id>/', blog_views.specific_post, name='specific-blog'),
    path('post/<int:post_id>/like/', blog_views.like_post, name='like_post'),
    path('post/<int:post_id>/comment/', blog_views.comment_post, name='comment_post'),
]
