from django.db import models

# Create your models here.
class TechStack(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateField()
    tech_stack = models.ManyToManyField(TechStack)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200, null=True, blank=True)
    issued_on = models.DateField()
    organisation = models.CharField(max_length=200)
    tech_stack = models.ManyToManyField(TechStack)

    class Meta:
        ordering = ['-issued_on']

    def __str__(self):
        return self.name

class Resume(models.Model):
    name = models.CharField(max_length=100)
    cv = models.FileField(upload_to='documents/')
    certificates = models.ManyToManyField(Certificate)

    def __str__(self):
        return self.name
#Meta is used to choose the ordering for the data returned to the view

