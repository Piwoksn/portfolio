# Generated by Django 4.2.5 on 2025-05-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_image_project_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='project'),
        ),
    ]
