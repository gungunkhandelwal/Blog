from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url (self):
        return reverse('index')

    
class Post(models.Model):
    title=models.CharField(max_length=300)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=100,default='coding')
    about=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    snippet=models.CharField(max_length=100,default='Read More..')
    img=models.ImageField(upload_to='static/img',default="")

    def __str__(self):
        return self.title +' -'+ str(self.author)
    
    def get_absolute_url (self):
        return reverse('index')
    

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    body=models.TextField()
    date_post=models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.post.title,self.name)
    def get_absolute_url (self):
        return reverse('index')
    
# class Contact(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField()
#     query=models.TextField()
#     def __str__(self):
#         return self.name 

#     def get_absolute_url (self):
#         return reverse('index')



