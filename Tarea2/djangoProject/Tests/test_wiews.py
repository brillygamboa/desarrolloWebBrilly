"""
Tests for views in djangoProject.

This module contains tests for the views in the djangoProject application.
"""

import pytest
from django.urls import reverse
from django.test import Client
from django.urls import reverse
from django.test import Client
from djangoProject import views  

@pytest.mark.django_db
def test_index_view():
    """
    Test the index view.

    This test ensures that the index view returns a 200 status code and renders the correct template.
    """
    client = Client()
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert 'index.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_resume_view():
    """
    Test the resume view.

    This test ensures that the resume view returns a 200 status code and renders the correct template.
    """
    client = Client()
    response = client.get(reverse('resume'))
    assert response.status_code == 200
    assert 'resume.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_about_view():
    """
    Test the about view.

    This test ensures that the about view returns a 200 status code and renders the correct template.
    """
    client = Client()
    response = client.get(reverse('about'))
    assert response.status_code == 200
    assert 'about.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_blog_view():
    """
    Test the blog view.

    This test ensures that the blog view returns a 200 status code and renders the correct template.
    """
    client = Client()
    response = client.get(reverse('blog'))
    assert response.status_code == 200
    assert 'blog.html' in [t.name for t in response.templates]
