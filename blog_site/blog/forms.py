from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ("author",'title', 'text')

        widget = {
            'author': forms.TextInput(attrs={"class":"form-text text-muted"}),
            'title': forms.TextInput(attrs={"class":"form-text text-muted"}),
            'text': forms.Textarea(attrs={"class":"form-control"}),
        }


class Comment(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ("author", "text")

        widget = {
            'author': forms.TextInput(attrs={"class":"form-text text-muted"}),
            'text': forms.Textarea(attrs={"class":"form-control"}),
        }