from django.forms import ModelForm
from .models import Post
from .models import Comment

class postForm(ModelForm):
     class Meta:
         model = Post
         exclude = ['id']

class commentform(ModelForm):
     class Meta:
         model = Comment
         exclude = ['id']
