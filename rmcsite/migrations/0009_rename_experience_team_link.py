# Generated by Django 4.0 on 2022-01-28 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmcsite', '0008_alter_team_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='experience',
            new_name='link',
        ),
    ]
