# Generated by Django 3.0.5 on 2020-04-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0010_auto_20200418_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_record',
            name='animal_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]