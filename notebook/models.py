from django.db import models
from django.utils.text import slugify


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    short_description = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255)
    page = models.ManyToManyField(Page, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class PageCategory(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.page.title + ' ' + self.category.name

    class Meta:
        verbose_name_plural = "Page Categories"
