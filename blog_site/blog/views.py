from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm


# Create your views here.
class AboutView(TemplateView):

    template_name = "blog/about.html"

class PostListView(ListView):

    model = Post

    def get_queryset(self) -> QuerySet[Any]:
        # __lte is a condition referring to "less than or equal to"
        # - in published_date means to be sorted in Descending Order: Most Recent blog post first!!!
        return Post.objects.filter(published_date__lte = timezone.now()).order_by("-published_date")
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class DraftListView(ListView, LoginRequiredMixin):
    model = Post
    login_url = "/login/"
    redirect_field_name = "blog/post_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(published_date__isnull=True).order_by("-created_date")


##############################################################################
##############################################################################

@login_required
def add_comment_on_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment = comment.post
            comment.save()
            return redirect('post_detail', {"pk":post.pk})
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {"form":form})

@login_required
def approve_comment_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve_comment()
    comment.save()

    return redirect('post_detail', pk= comment.post.pk)\
    
@login_required
def delete_comment(request,pk):

    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail', pk= post_pk)

@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish_post()
    return render("post_detail", pk= post.pk)