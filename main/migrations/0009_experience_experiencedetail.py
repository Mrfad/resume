# Generated by Django 3.2.7 on 2021-09-18 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_fact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceDEtail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('from_year', models.DateField(blank=True, null=True)),
                ('to_year', models.DateField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('duty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.experiencedetail')),
            ],
        ),
    ]