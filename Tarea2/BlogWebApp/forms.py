from django import forms

class MessageForm(forms.Form):
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Name', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
