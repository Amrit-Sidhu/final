# Generated by Django 3.0.5 on 2020-04-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0020_animal_record_farmer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccination',
            name='is_done',
        ),
        migrations.AddField(
            model_name='vaccination',
            name='due_date',
            field=models.DateField(default='2020-02-02'),
        ),
        migrations.AddField(
            model_name='vaccination',
            name='tag_no',
            field=models.CharField(default='no selected', max_length=34),
        ),
    ]