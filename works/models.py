from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from markdown import markdown
from django.db.models.functions import Coalesce
from django.db.models.aggregates import Max


class Work(models.Model):
    title = models.CharField(_('work'), max_length=100)
    order = models.PositiveIntegerField(default=0, editable=True)
    slug = models.SlugField(unique=True, max_length=255)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    banner = models.ImageField(upload_to="work", blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    class Meta():
        ordering = ['-order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if not self.order:
            self.order = Work.objects.aggregate(max_order=Coalesce(Max('order'), 0))['max_order'] + 1
        super(Work, self).save(*args, **kwargs)

    @property
    def html_content(self):
        content = markdown(
            self.content, extensions=['fenced_code'])
        return content

    @property
    def banner_append(self):
        if self.banner:
            banner = self.banner
            google_storage = 'storages.backends.gcloud.GoogleCloudStorage'
            if settings.DEFAULT_FILE_STORAGE == google_storage:
                return f"{settings.GS_URL}{banner.name}"
            return banner.url
        return None


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    work = models.ManyToManyField(
        Work, related_name="techs",
        blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="work")
    work = models.ForeignKey(Work, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def image_append(self):
        image = self.image
        google_storage = 'storages.backends.gcloud.GoogleCloudStorage'
        if settings.DEFAULT_FILE_STORAGE == google_storage:
            return f"{settings.GS_URL}{image.name}"
        return image.url
