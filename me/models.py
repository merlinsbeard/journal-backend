from django.db import models
from django.core.cache import cache
from markdown import markdown


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)


class Me(SingletonModel):
    name = models.CharField(max_length=255, default="Name")

    profile = models.ImageField(
        upload_to="me", blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    gitlab = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Me",
        verbose_name_plural = "Me"

    @property
    def about_me_html(self):
        about_me = markdown(
            self.about_me, extensions=['fenced_code'])
        return about_me
