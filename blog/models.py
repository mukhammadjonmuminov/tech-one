from django.db import models
from django.utils import timezone
from .helpers import SaveImages, Status
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(verbose_name="Post", max_length=255)
    slug = models.SlugField(verbose_name='Slug', max_length=255)
    image = models.ImageField(verbose_name='Images', upload_to=SaveImages.post_images_path, blank=True, null=True)
    content = models.TextField(verbose_name='Content')
    publish = models.DateTimeField(verbose_name='Publish', default=timezone.now)
    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True)
    status = models.CharField(verbose_name='Status', max_length=2, choices=Status.PublishRoles.choices, default=Status.PublishRoles.DRAFT)

    class Meta:
        ordering = ['-publish']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def get_queryset(self):
        return Post.objects.all()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.user} -- {self.text}"