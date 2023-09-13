from rest_framework import serializers
from .models import Person, validate_text


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, validators=[validate_text])
    age = serializers.CharField(validators=[validate_text])
    place_of_birth = serializers.CharField(max_length=50, default=1)

    class Meta:
        model = Person
        fields = ('__all__')


# curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/user_id/ -d '{"name":"John","age":30,"place_of_birth":"London"}'
# curl -X GET http://127.0.0.1:8000/api/user_id/
# curl -X PUT -H "Content-Type: application/json" http://127.0.0.1:8000/api/user_id/ -d '{"name":"Updated Name","age":35,"place_of_birth":"New York"}'
# curl -X DELETE http://127.0.0.1:8000/api/user_id/