# Generated by Django 2.2.3 on 2019-09-10 10:04

from django.db import migrations, models
import nafir.models


class Migration(migrations.Migration):

    dependencies = [
        ('nafir', '0003_auto_20190910_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='favicon',
            field=models.ImageField(upload_to=nafir.models.favicon_upload_path),
        ),
        migrations.AlterField(
            model_name='info',
            name='picture',
            field=models.ImageField(upload_to=nafir.models.profile_picture_upload_path),
        ),
    ]
