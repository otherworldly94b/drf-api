# Generated by Django 3.2.4 on 2024-04-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_yjhef1', upload_to='images/'),
        ),
    ]