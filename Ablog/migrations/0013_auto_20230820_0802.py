# Generated by Django 3.2.20 on 2023-08-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ablog', '0012_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to='ablog/img'),
        ),
    ]
