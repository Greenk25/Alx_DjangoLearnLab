# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from .models import Post
from taggit.managers import TaggableManager
class Post(models.Model):
    # Your existing fields...
    tags = TaggableManager()
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    # Your existing fields...
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
    content = models.TextField()  # Text of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set when updated

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','tags']

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
lass Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
