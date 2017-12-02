from django import forms
from .models import Post

class PostForm(forms.ModelForm):
     class Meta:
         model = Post
         fields = [ 'title', 'text', 'photo']  

class LinkForm(forms.Form):
	link = forms.CharField(label='Link 2 ur photo' )               