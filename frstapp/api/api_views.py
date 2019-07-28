from rest_framework import viewsets
from .. import models
from . import serializers


class DModelViewset(viewsets.ModelViewSet):
	queryset = models.DModel.objects.all()
	serializer_class = serializers.DModelSerializer
	

