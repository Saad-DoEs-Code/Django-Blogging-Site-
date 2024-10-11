from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>.remove/", views.PostDeleteView.as_view(), name= "post_delete"),
    path("draft/", views.DraftListView.as_view(), name="post_draft_list"),
    path("post/<int:pk>/comments", views.add_comment_on_post, name="add_comment"),
    path("comment/<int:pk>/approve", views.approve_comment_view, name="approve_comment"),
    path("comment/<int:pk>/remove", views.delete_comment, name="delete_comment"), 
    path("post/<int:pk>/piblish", views.publish_post, name="post_publish")
]