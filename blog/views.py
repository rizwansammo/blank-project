from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, "blog/blog_list.html", {"posts": posts})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/blog_detail.html", {"post": post})