# Generated by Django 3.2 on 2022-07-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220620_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='details',
            new_name='message',
        ),
        migrations.AddField(
            model_name='contactform',
            name='subject',
            field=models.CharField(default=False, max_length=255),
        ),
    ]
