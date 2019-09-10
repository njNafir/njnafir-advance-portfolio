# Generated by Django 2.2.3 on 2019-07-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HireContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=120)),
                ('project_budget', models.CharField(max_length=120)),
                ('completion_date', models.CharField(blank=True, max_length=32, null=True)),
                ('project_detail', models.TextField()),
            ],
        ),
    ]