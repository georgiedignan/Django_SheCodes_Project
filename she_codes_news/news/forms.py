from django import forms
from .models import NewsStory
from django.forms import ModelForm, TextInput, Textarea


#allow Django to infer from all the form fields and validation from a model
class StoryForm(forms.ModelForm):
    class Meta:
        #list of fields to be included in the field
        model = NewsStory
        fields = ['title','pub_date','content','image_url']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Selecta date','type':'date'}),

            'title': forms.TextInput(attrs={
                'class': "form-control",
                }),

            'image_url': forms.TextInput(attrs={
                'class': "form-control",
                }),

            'content': forms.Textarea(attrs={
                'id': "WriteStory",
                }),
        }
      




