# Generated by Django 5.0.4 on 2024-07-26 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
