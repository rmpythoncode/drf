# Generated by Django 4.0.6 on 2022-08-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha1', models.CharField(max_length=200)),
                ('linha2', models.CharField(blank=True, max_length=200, null=True)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('latitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
