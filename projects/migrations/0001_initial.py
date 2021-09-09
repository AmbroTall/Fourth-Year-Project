# Generated by Django 3.2.3 on 2021-06-23 14:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('proj_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('proj_img', models.ImageField(blank=True, default='images_1.jpg', null=True, upload_to='images')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('project_by', models.CharField(max_length=50)),
                ('date_published', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]