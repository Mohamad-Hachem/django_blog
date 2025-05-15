from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404


# showing all posts that are published
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


# showing the details of a single post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post':post})
