
from typing import Any
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



class HomeView(ListView):
   model=Post
   template_name='index.html'
   ordering=['post_date']

   def get_context_data(self,*args, **kwargs):
      cat_menu=Category.objects.all()
      context= super(HomeView,self).get_context_data(*args,**kwargs)
      context["cat_menu"]=cat_menu
      return context
def CategoryListView(request):
   category_list=Category.objects.all()
   return render(request,'category_list.html',{'category_list':category_list})


def CategoryView(request,cats): 
   category_post=Post.objects.filter(category=cats)
   return render(request,'category.html',{'cats':cats.title,'category_post':category_post})


class ContentView(DetailView):
    model=Post
    template_name='content.html'

    def get_context_data(self,*args, **kwargs):
      cat_menu=Category.objects.all()
      context= super(ContentView,self).get_context_data(*args,**kwargs)
      context["cat_menu"]=cat_menu
      return context

class AddPost(CreateView):
   model=Post
   form_class=PostForm
   template_name='add_post.html'

class AddComment(CreateView):
   model=Comment
   template_name='add_comment.html'
   fields='__all__'

class AddCategory(CreateView): 
   model=Category
   template_name='add_category.html'
   fields='__all__'

class UpdatePost(UpdateView):
   model=Post
   template_name='update_post.html'
   fields=['title','about','img']

class DeletePost(DeleteView):
   model=Post
   template_name='delete_post.html'
   success_url=reverse_lazy('index')


def ContactUs(request):
   return render(request,'contact.html')
  


   

