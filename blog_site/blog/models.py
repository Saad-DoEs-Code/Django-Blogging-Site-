from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    # auth.User refers to the Super User, that was created in "auth" app.
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)


    def publish_post(self):
        self.published_date = timezone.now()
        self.save()

    def show_approved_comments(self):
        return self.comments.filter(is_approved = True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    # This related_name = "comments" will be pointing to the approved_comments() of Post Model.
    post = models.ForeignKey("blog.Post", related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    is_approved = models.BooleanField(default=False)

    def approve_comment(self):
        self.is_approved = True
        self.save()

    def __str__(self) -> str:
        return self.text