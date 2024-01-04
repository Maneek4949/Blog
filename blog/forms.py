from blog.models import Post,Comment,Like, Category
from django import forms
from tinymce.widgets import TinyMCE



class PostForm(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Select a Category')
    class Meta:
        model = Post
        fields = ('title', 'text','cover_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'TitleInput form-control' , 'placeholder': 'Title'}),
            'cover_image':forms.ClearableFileInput(),
           'text': TinyMCE(attrs={'class': 'TextInput editable form-control'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text':forms.TextInput(attrs={'class':'commentBox mb-3 form-control','placeholder': 'Comment'})
        }

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ('value',)
        widgets = {
            'value': forms.HiddenInput(),
        }
