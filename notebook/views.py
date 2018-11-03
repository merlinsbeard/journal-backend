from .serializers import PageSerializer, CategorySerializer
from .models import Page, PageCategory, Category
from rest_framework import generics


class PageList(generics.ListAPIView):
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer


class PageDetail(generics.RetrieveAPIView):
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer
    lookup_field = "slug"


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
