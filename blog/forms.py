from blog.models import Post,Comment
from django import forms



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('author','title','text')

        widgets={
            'author':forms.Select(attrs={'class':'form-control '}),
            'title':forms.TextInput(attrs={'class':'TitleInput form-control '}),
            'text':forms.Textarea(attrs={'class':'TextInput editable form-control'})
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control '}),
            'text':forms.Textarea(attrs={'class':'TextInput editable form-control'})
        }
