from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_text(text):
    # charvalid = r'^[A-Za-z]*$'
    # if not re.match(text, str):
    #     raise ValidationError('Field should only contain letters.')
    print("validation", text)
    if type(text) != type("str"):
        raise ValidationError("fields must be a string")
    print (type(text))



class Person(models.Model):
    name = models.CharField(max_length=50, validators=[validate_text])
    age = models.CharField(max_length=50, null=True, validators=[validate_text])
    place_of_birth = models.CharField(max_length=50, default=1)
