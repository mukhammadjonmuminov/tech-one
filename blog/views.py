from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView
from .models import Post

class BlogListView(View):
    def get(self, request):
        posts = Post.get_queryset
        context = {
            "posts": posts,
        }
        return render(request, 'blog.html', context)

class BlogDetailView(View):
    def get(self, request):
        singles = Post.get_queryset
        context = {
            "singles": singles,
        }
        return render(request, 'single.html', context)

class ContactView(View):
    def get(self, request):
        singles = Post.get_queryset
        context = {
            "singles": singles,
        }
        return render(request, 'contact.html', context)
