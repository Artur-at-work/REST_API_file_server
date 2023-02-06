from rest_framework import serializers
from crud.models import VideoModel


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoModel
        exclude = ('file', 'mime_type', 'id',)

