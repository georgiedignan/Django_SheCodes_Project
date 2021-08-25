from django import forms
from django.forms import ModelForm
from .models import NewsStory

#allow Django to infer from all the form fields and validation from a model
class StoryForm(ModelForm):
    class Meta:
        #list of fields to be included in the field
        model = NewsStory
        fields = ['title','pub_date','content','image_url']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Selecta date','type':'date'}),
        }
      




