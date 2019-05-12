import markdown2
from rest_framework import serializers
from .models import Page, Category
from django.conf import settings


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):

    categories = serializers.SlugRelatedField(
                    many=True,
                    read_only=True,
                    slug_field='name')
    banner = serializers.ImageField(max_length=None)
    content = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = (
            'title',
            'slug',
            'short_description',
            'content',
            'date_created',
            'date_updated',
            'categories',
            'banner',
        )

    def get_content(self, obj):
        content = markdown2.markdown(obj.content, extras=settings.MARKDOWN_EXTRAS)
        return content
