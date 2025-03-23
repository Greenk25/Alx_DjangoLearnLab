from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagWidget  # Import TagWidget for handling tags
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Include only the content field in the form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include the tags field
        widgets = {
            'tags': TagWidget(),  # Use the TagWidget to handle tags
        }
