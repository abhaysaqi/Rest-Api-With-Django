from myapp.models import Movie
from rest_framework import serializers # They convert complex data types, such as Django model instances, into native Python data types that can be easily serialized to formats like JSON.

class MovieSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model=Movie
        fields=('name','desc','rating','image')

