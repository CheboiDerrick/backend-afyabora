from rest_framework import serializers
from .models import userdata

class usersSerializer(serializers.ModelSerializer):
	class Meta:
		model = userdata
		fields = '__all__'
