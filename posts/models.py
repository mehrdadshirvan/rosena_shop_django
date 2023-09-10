from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=150)
    slug = models.SlugField(default="",null=False, blank=True,editable=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('blog-single-post', args=[self.slug])

    def __str__(self):
        return f"{self.name} ({self.id})"