# Generated by Django 4.2.4 on 2023-08-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(help_text='Описание', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='post_date',
            field=models.DateField(null=True),
        ),
    ]
