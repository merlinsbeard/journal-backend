from .serializers import PageSerializer, CategorySerializer
from .models import Page, PageCategory, Category
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer


class PageDetail(generics.RetrieveUpdateAPIView):
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer
    lookup_field = "slug"


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
