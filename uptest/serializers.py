from rest_framework import serializers
from .models import *


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectInfo
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('project', 'image')