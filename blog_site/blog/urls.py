from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("post/new/", views.PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>.remove/", views.PostDeleteView.as_view(), name= "post_delete"),
    path("draft/", views.DraftListView.as_view(), name="post_draft_list"),
]