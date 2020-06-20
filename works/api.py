import logging
from rest_framework import serializers, viewsets, mixins
from rest_framework.response import Response
from .models import Work, Image, Technology


logger = logging.getLogger(__name__)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'


class WorkViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    class WorkSerializer(serializers.ModelSerializer):
        images = ImageSerializer(many=True)
        techs = TechnologySerializer(many=True)

        class Meta:
            model = Work
            fields = '__all__'

    queryset = Work.objects.all()
    serializer_class = WorkSerializer
