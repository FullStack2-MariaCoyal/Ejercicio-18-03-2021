# Generated by Django 3.1.7 on 2021-03-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='owner',
            field=models.CharField(choices=[('C', 'Carlos Cuahutemoc'), ('D', 'Dimitry Glujvosky')], default='', max_length=100),
        ),
    ]