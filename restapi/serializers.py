from rest_framework import serializers
from .models import Person, validate_text


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, validators=[validate_text])
    age = serializers.CharField(validators=[validate_text])
    place_of_birth = serializers.CharField(max_length=50, default=1)

    class Meta:
        model = Person
        fields = ('__all__')
