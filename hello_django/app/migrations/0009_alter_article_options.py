# Generated by Django 3.2.5 on 2021-08-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210805_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_time']},
        ),
    ]
