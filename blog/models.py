from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    excerpt = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            idx = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                idx += 1
                slug = f"{base}-{idx}"
            self.slug = slug
        if not self.excerpt and self.body:
            self.excerpt = (self.body[:297] + "...") if len(self.body) > 300 else self.body
        super().save(*args, **kwargs)