import logging
from rest_framework import serializers, viewsets, mixins
from .models import Work, Image, Technology


logger = logging.getLogger(__name__)


def create_or_get_tech(work_instance, techs_data=[]):
    if techs_data:
        for tech_data in techs_data:
            tech, _ = Technology.objects.get_or_create(
                name=tech_data)
            tech.work.add(work_instance)
    return


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name']
        extra_kwargs = {
            'name': {'validators': []}
        }


class WorkViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    class WorkSerializer(serializers.ModelSerializer):
        images = ImageSerializer(many=True, read_only=True)
        techs = TechnologySerializer(many=True, validators=None)
        order = serializers.IntegerField(required=False)
        slug = serializers.SlugField(required=False)
        techs = serializers.SlugRelatedField(
            many=True, read_only=False, write_only=False,
            queryset=Technology.objects.all(), slug_field="name")

        class Meta:
            model = Work
            fields = '__all__'
            extra_kwargs = {
                'techs': {'validators': []}
            }

        def create(self, validated_data):
            techs_data = validated_data.pop('techs', '')
            work = Work.objects.create(**validated_data)
            create_or_get_tech(work, techs_data)
            return work

    def update(self, request, *args, **kwargs):
        """ Create or get the tech tag first then perform the update operation """
        techs_data = request.data.get('techs', [])
        create_or_get_tech(self.get_object(), techs_data)
        return super().update(request, *args, **kwargs)

    queryset = Work.objects.all()
    serializer_class = WorkSerializer
