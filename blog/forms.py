from django import forms
from .models import PostBlog


class BlogForm(forms.ModelForm):
    """ Form to create blog post """
    class Meta:
        model = PostBlog
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
