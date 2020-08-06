# Generated by Django 3.0 on 2020-08-06 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200806_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='owner',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='api.Post'),
            preserve_default=False,
        ),
    ]
