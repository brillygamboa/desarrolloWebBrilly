from django import forms
from .models import BlogPost


class MessageForm(forms.Form):
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Name', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'thumbnail_url', 'preview_text', 'text', 'readingTimeInMinutes', 'author']