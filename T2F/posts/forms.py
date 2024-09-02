from .models import Post, Comment, Like
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'group', 'image']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
