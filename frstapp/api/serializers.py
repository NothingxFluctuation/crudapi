from rest_framework import serializers
from ..models import DModel

class DModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = DModel
		fields = ('id','name','description','driver','host','port','username','password')
		
