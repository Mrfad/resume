# Generated by Django 3.2.7 on 2021-09-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210918_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
