# Generated by Django 5.0.6 on 2025-01-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_quiz_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_option',
            field=models.CharField(default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
