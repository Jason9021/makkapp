# Generated by Django 5.0.3 on 2024-04-02 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]