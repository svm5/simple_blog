# Generated by Django 4.2.4 on 2023-08-25 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_options_blog_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-post_date']},
        ),
    ]
