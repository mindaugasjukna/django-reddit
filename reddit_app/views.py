from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def index(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        post = Post()
        post.title = title
        post.text = text
        post.save()

    posts = Post.objects.filter(user=request.user)
    context = {
        'posts': posts,
        'user': request.user
    }

    return render(request, 'reddit_app/index.html', context)


@login_required
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


@login_required
def delete_post(request):
    pk = request.POST["pk"]
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return HttpResponseRedirect(reverse('reddit_app:index'))
