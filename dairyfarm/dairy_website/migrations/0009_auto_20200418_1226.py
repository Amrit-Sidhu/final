# Generated by Django 3.0.5 on 2020-04-18 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0008_auto_20200418_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_record',
            name='animal_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
