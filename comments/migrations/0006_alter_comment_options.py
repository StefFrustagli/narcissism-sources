# Generated by Django 4.2.10 on 2024-03-08 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_remove_comment_content_remove_comment_source'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
    ]
