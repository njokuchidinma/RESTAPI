# Generated by Django 4.2.5 on 2023-09-13 07:29

from django.db import migrations, models
import restapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_person_age_person_place_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.CharField(max_length=50, null=True, validators=[restapi.models.validate_text]),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50, validators=[restapi.models.validate_text]),
        ),
    ]
