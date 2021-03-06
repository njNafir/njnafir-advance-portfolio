# Generated by Django 2.2.3 on 2019-07-26 09:26

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('thumbnail', models.ImageField(upload_to=blog.models.post_thumb_upload_path)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default='md_nafir', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('blog_category', models.ManyToManyField(to='category.BlogCategory')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
