# Generated by Django 3.2.20 on 2023-08-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ablog', '0004_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
