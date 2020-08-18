# Generated by Django 3.0.9 on 2020-08-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0003_auto_20200805_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuemodel',
            name='create_by',
        ),
        migrations.AddField(
            model_name='issuemodel',
            name='created_by',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='issuemodel',
            name='environment',
            field=models.CharField(choices=[('Prod', 'Production')], default='Prod', max_length=20),
        ),
        migrations.AlterField(
            model_name='issuemodel',
            name='logged_by',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
