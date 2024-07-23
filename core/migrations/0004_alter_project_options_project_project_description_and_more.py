# Generated by Django 5.0.6 on 2024-05-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_project_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('order',), 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='project_description',
            field=models.TextField(blank=True, default='', verbose_name='Project Description'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Project Type'),
        ),
    ]
