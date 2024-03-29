# Generated by Django 4.2.7 on 2024-01-15 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_picture_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pictures',
        ),
        migrations.AddField(
            model_name='picture',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='blogapp.project'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='project_pictures/'),
        ),
    ]
