from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post


def index(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        post = Post()
        post.title = title
        post.text = text
        post.save()

    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'reddit_app/index.html', context)


def change_status(request):
    pk = request.POST["pk"]
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        title = request.POST["title_update"]
        post.title = title
        text = request.POST["text_update"]
        post.text = text
    post.save()

    return HttpResponseRedirect(reverse('reddit_app:index'))


def delete_post(request):
    pk = request.POST["pk"]
    post = get_object_or_404(Post, pk=pk)
