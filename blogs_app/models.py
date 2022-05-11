from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE,)
    img=models.ImageField(upload_to='images/',blank=True,null=True)
    body=models.TextField()
    

    def __str__(self):
        return self.title[:20]
    
    def get_absolute_url(self):
        return reverse("post_details", args=[str(self.id)])
    