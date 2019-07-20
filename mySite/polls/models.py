from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    slug = models.SlugField()
    body = models.CharField(max_length=500)
    category = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s'%(self.title,self.body,self.category)
