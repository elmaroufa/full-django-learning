from django.shortcuts import render
from django.http import Http404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,
    'blog/post/list.html',
    {'posts' : posts}
    )

def post_detail(request, id):
    pass