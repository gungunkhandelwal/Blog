from django import forms
from .models import Post,Category


choices=Category.objects.all().values_list('name','name')
choice_list=[]
for item in choices:
    choice_list.append(item)
    

class PostForm(forms.ModelForm):
    class Meta:  
        model=Post
        fields=('title','author','category','about','snippet','img')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':"",'id':'gungun','type':'hidden'}),
            #'author':forms.Select(attrs={'class':'form-contol'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'about':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
            }