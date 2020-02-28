from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.http import HttpResponse, Http404
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesnotExist:
        raise Http404('Page not found')
    return render(request, 'blog/post_detail.html', {'post': post})
