# djangoProject/Tests/test_views.py
import pytest
from django.urls import reverse
from django.test import Client
from django.urls import reverse
from django.test import Client
from djangoProject import views  

@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_resume_view():
    client = Client()
    response = client.get(reverse('resume'))
    assert response.status_code == 200
    assert 'resume.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_about_view():
    client = Client()
    response = client.get(reverse('about'))
    assert response.status_code == 200
    assert 'about.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_blog_view():
    client = Client()
    response = client.get(reverse('blog'))
    assert response.status_code == 200
    assert 'blog.html' in [t.name for t in response.templates]
