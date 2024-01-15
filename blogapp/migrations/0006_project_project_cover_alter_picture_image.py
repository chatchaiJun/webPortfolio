# Generated by Django 4.2.7 on 2024-01-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_remove_project_pictures_picture_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_cover',
            field=models.ImageField(blank=True, upload_to='project_pictures'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='project_pictures'),
        ),
    ]
