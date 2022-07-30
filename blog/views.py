# from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.urls import reverse_lazy
# from django import forms

from .models import Post
from .forms import NewPostForm


class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'
    context_object_name = 'form'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('post_list')





