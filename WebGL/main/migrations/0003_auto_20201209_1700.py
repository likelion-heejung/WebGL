# Generated by Django 3.1.4 on 2020-12-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201209_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webgl_project',
            old_name='url',
            new_name='project_url',
        ),
        migrations.AlterField(
            model_name='webgl_project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnail'),
        ),
    ]