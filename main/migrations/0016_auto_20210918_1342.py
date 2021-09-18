# Generated by Django 3.2.7 on 2021-09-18 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_certification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='certification',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.collge'),
        ),
    ]