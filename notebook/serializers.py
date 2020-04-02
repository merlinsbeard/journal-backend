import markdown
from rest_framework import serializers
from .models import Page, Category, Tag
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class PageSerializer(serializers.ModelSerializer):

    banner = serializers.ImageField(max_length=None, required=False),
    slug= serializers.SlugField(required=False)
    content_html = serializers.ReadOnlyField(source="html_content")
    tags = TagSerializer(many=True)
    content = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = (
            'title',
            'is_active',
            'date_created',
            'date_updated',
            'slug',
            'short_description',
            'content',
            'content_html',
            'banner',
            'tags',
        )
        depth = 1

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        page = Page.objects.create(**validated_data)

        for t in tags:
            tag, _ = Tag.objects.get_or_create(
                name=t.get('name'),
            )
            page.tags.add(tag)
        return page

    def get_content(self, obj):
        return obj.html_content