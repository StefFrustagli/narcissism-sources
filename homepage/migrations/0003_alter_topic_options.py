# Generated by Django 4.2.10 on 2024-03-08 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_topic_options_topic_created_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['created_on']},
        ),
    ]
