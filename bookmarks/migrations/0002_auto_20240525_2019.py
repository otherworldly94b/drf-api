# Generated by Django 3.2.4 on 2024-05-25 20:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='post',
            new_name='bookmark_post',
        ),
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('owner', 'bookmark_post')},
        ),
    ]
