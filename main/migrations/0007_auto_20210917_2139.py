# Generated by Django 3.2.7 on 2021-09-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210917_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='icon',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='fact',
            name='number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
