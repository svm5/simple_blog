# Generated by Django 4.2.4 on 2023-08-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bloger_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
