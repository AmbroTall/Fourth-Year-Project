# Generated by Django 3.2.3 on 2021-09-07 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_alter_advertisements_advert_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisements',
            old_name='footer_advert',
            new_name='news_advert',
        ),
    ]