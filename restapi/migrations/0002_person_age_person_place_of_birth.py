# Generated by Django 4.2.5 on 2023-09-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='place_of_birth',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
