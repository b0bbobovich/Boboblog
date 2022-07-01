from django import forms as basic_forms
from . import models as my_models


def get_choice_list():
    choices = my_models.Category.objects.all().values_list('name', 'name')
    choice_list = []
    for item in choices:
        choice_list.append(item)
    return choice_list

class PostForm(basic_forms.ModelForm):
    class Meta:
        model = my_models.Post
        fields = ['title', 'author', 'category', 'body', 'snippet', 'header_image']

        widgets = {
            'title': basic_forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Enter post title here',
                'required': 'required',
                'onkeyup': "textCounter(this,'counter1',255)"}),
            'author': basic_forms.TextInput(attrs={
                "class": 'form-control',
                'value': '',
                'id': 'user_id',
                'type': 'hidden'}),
            'category': basic_forms.Select(choices=get_choice_list(), attrs={
                "class": 'form-control'}),
            'body': basic_forms.Textarea(attrs={
                "class": 'form-control',
                'required': 'required'}),
            'snippet': basic_forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Enter post description for home page ',
                'required': 'required',
                'onkeyup': "textCounter(this,'counter2',100)"})
        }

        header_image = basic_forms.ImageField(
            label='Header image for your post')

class EditForm(basic_forms.ModelForm):
    class Meta:
        model = my_models.Post
        fields = ['title', 'category', 'body', 'snippet', 'header_image']

        widgets = {
            'title': basic_forms.TextInput(attrs={"class": 'form-control'}),
            'category': basic_forms.Select(choices=get_choice_list(), attrs={"class": 'form-control'}),
            'body': basic_forms.Textarea(attrs={"class": 'form-control'}),
            'snippet': basic_forms.Textarea(attrs={"class": 'form-control'})
        }


class CommentForm(basic_forms.ModelForm):
    class Meta:
        model = my_models.Comment
        fields = ['name', 'body']

        widgets = {
            'name': basic_forms.TextInput(attrs={"class": 'form-control'}),
            'body': basic_forms.Textarea(attrs={"class": 'form-control'}),

        }