from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title   =   models.CharField(max_length=200)
    slug    =   models.SlugField(unique=True, blank=True)
    body    =   models.TextField()
    created =   models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title