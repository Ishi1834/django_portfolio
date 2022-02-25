from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title