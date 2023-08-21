from django.urls import path
from .views import HomeView,ContentView,AddPost,UpdatePost,DeletePost,AddCategory,CategoryView,CategoryListView,AddComment,ContactUs
urlpatterns = [
    path('',HomeView.as_view(),name ='index'),
    path('content/<int:pk>',ContentView.as_view(),name ='content'),
    path('add_post/',AddPost.as_view(),name='Add_post'),
    path('add_category/',AddCategory.as_view(),name='Add_category'),
    path('content/edit/<int:pk>',UpdatePost.as_view(),name='updatepost'),
    path('content/<int:pk>/remove',DeletePost.as_view(),name='deletepost'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category_list/',CategoryListView,name='category_list'),
    path('content/<int:pk>/comment/',AddComment.as_view(),name='add_comment'),
    path('contact',ContactUs,name='contact'),
] 