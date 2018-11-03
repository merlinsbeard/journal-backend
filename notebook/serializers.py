from rest_framework import serializers
from .models import Page, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):

    categories = serializers.SlugRelatedField(
                    many=True,
                    read_only=True,
                    slug_field='name')

    class Meta:
        model = Page
        fields = (
            'title',
            'slug',
            'short_description',
            'content',
            'date_created',
            'date_updated',
            'categories'
        )
