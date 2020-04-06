from .serializers import PageSerializer, CategorySerializer
from .models import Page, PageCategory, Category
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated


class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.filter(is_active=True).order_by('-date_updated')
    serializer_class = PageSerializer


class PageDetail(generics.RetrieveUpdateAPIView):
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer
    lookup_field = "slug"


class CategoryList(generics.ListAPIView, generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# Ability to make tags
# Ability to add tags

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.filter(is_active=True).order_by('-date_updated')
    serializer_class = PageSerializer
    lookup_field = 'slug'