# Generated by Django 3.2 on 2022-06-09 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0005_auto_20220609_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
