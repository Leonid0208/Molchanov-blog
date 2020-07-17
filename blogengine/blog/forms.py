from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})

        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be create')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug may not be create')
        return new_slug

    def clean_title(self):
        new_title = self.cleaned_data['title']
        if Tag.objects.filter(title__iexact=new_title).count():
            raise ValidationError('Title may not be create')
        return new_title


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be create')
        return new_slug
