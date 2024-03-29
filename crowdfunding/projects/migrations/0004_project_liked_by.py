# Generated by Django 4.1.5 on 2023-01-26 11:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_alter_project_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
