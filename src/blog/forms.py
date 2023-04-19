from django import forms
from .models import Photo, Blog

class PhotoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['onchange'] = 'preview();'

    class Meta:
        model = Photo
        fields = ('image', 'caption')

class BlogForm(forms.ModelForm):
    edit = forms.BooleanField(initial=True)

    class Meta:
        model = Blog
        fields = ('title', 'content')
        widgets = {
            'content': forms.Textarea(attrs={
                'cols': 50, 'rows': 10
            }),
            'edit': forms.HiddenInput
        }

class DeleteBlogForm(forms.Form):
    delete = forms.BooleanField(initial=True)

    class Meta:
        widgets = {
            'delete': forms.HiddenInput
        }
