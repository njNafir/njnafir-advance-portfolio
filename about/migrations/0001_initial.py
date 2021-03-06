# Generated by Django 2.2.3 on 2019-07-26 09:21

import about.models
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManOverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('website', models.CharField(blank=True, max_length=30, null=True)),
                ('address_line_1', models.CharField(max_length=120)),
                ('address_line_2', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=13)),
                ('objective', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('man_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.ManOverview')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=120)),
                ('certificate', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Md_Nadir\\Envs\\njnafir\\src\\njNafir\\njNafir_staticfiles_dirs\\med_prot_file'), upload_to=about.models.qualification_certificate_upload_path)),
                ('man_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.ManOverview')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_detail', models.CharField(max_length=255)),
                ('man_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.ManOverview')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('man_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.ManOverview')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=32)),
                ('interest_type', models.CharField(blank=True, max_length=20, null=True)),
                ('man_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.ManOverview')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=120)),
                ('year', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('institute', models.CharField(blank=True, max_length=120, null=True)),
                ('result', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('certificate', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Md_Nadir\\Envs\\njnafir\\src\\njNafir\\njNafir_staticfiles_dirs\\med_prot_file'), upload_to=about.models.education_certificate_upload_path)),
                ('man_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.ManOverview')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_detail', models.CharField(max_length=255)),
                ('prove_file', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Md_Nadir\\Envs\\njnafir\\src\\njNafir\\njNafir_staticfiles_dirs\\med_prot_file'), upload_to=about.models.award_certificate_upload_path)),
                ('man_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.ManOverview')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=120)),
                ('institute', models.CharField(max_length=120)),
                ('department', models.CharField(blank=True, max_length=120, null=True)),
                ('start_date', models.CharField(blank=True, max_length=12, null=True)),
                ('end_date', models.CharField(blank=True, max_length=12, null=True)),
                ('man_overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.ManOverview')),
            ],
        ),
    ]
