# Generated by Django 3.2.7 on 2021-09-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_experience_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='present',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]