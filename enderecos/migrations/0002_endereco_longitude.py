# Generated by Django 4.0.6 on 2022-08-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
