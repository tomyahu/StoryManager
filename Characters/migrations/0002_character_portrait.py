# Generated by Django 2.2.1 on 2020-02-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='portrait',
            field=models.ImageField(default='images/character_portraits/default.png', upload_to='images/character_portraits'),
        ),
    ]
