from rest_framework import serializers
from .models import Stream

# serializer 1 for model 1:
class StreamSerializer(serializers.ModelSerializer):
    
    def validate_stream_name(self, value):
        valid_choices = ['cse', 'ece', 'eee']
        if value not in valid_choices:
            raise serializers.ValidationError("Invalid stream name. Choose from 'cse', 'ece', 'eee'.")
        return value
    
    def validate_Stream_Existence(self, data):
        # Check if the stream_name already exists
        if 'stream_name' in data:
            stream_name = data['stream_name']
            if Stream.objects.filter(stream_name=stream_name).exists():
                raise serializers.ValidationError("Stream name '{}' already exists.".format(stream_name))
        return data
    
    class Meta:
        model = Stream
        fields = ['id', 'stream_name']

# serializer 2 for model 2:
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    stream_id = serializers.IntegerField(write_only=True, min_value=0)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'stream_id']

# serializer 3 for model 3:
from .models import Availability

class AvailabilitySerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField(write_only=True, min_value=0)
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Availability
        fields = ['id', 'book_id', 'quantity', 'available_status']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")
        elif not str(value).isdigit():
            raise serializers.ValidationError("Quantity must consist only of digits.")
        return value
