from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """ To add fields on comment form """

    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """ To add fields on post form """

    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'featured_image',)
