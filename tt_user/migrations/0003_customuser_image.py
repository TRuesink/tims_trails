# Generated by Django 3.0.8 on 2020-07-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0002_customuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
