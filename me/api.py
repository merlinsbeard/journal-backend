import logging
from rest_framework import serializers, viewsets, mixins
from rest_framework.response import Response
from .models import Me

logger = logging.getLogger(__name__)


class MeViewset(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    class MeSerializer(serializers.ModelSerializer):
        about_me_html = serializers.ReadOnlyField()

        class Meta:
            model = Me
            fields = (
                "id",
                "name",
                "profile",
                "about_me_html",
                "title",
                "email",
                "about_me",
                "mobile",
                "github",
                "gitlab"
            )

    queryset = Me.objects.all()
    serializer_class = MeSerializer

    def get_object(self):
        return Me.objects.get()

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(Me.objects.get())
        return Response(serializer.data)
