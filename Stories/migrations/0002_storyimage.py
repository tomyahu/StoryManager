# Generated by Django 2.2.1 on 2020-02-12 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='stories/story_images')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Stories.Story')),
            ],
        ),
    ]
