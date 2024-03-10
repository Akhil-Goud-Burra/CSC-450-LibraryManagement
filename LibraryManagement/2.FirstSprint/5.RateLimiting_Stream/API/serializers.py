from rest_framework import serializers

# serializer 1 for model 1:
from .models import Stream

class StreamSerializer(serializers.ModelSerializer):
    class Meta:

        model = Stream
        fields = ['id', 'stream_name']