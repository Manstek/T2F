# Generated by Django 4.2.15 on 2024-08-26 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'группа', 'verbose_name_plural': 'Группы'},
        ),
    ]
