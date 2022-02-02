# Generated by Django 3.0.5 on 2020-05-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_website', '0026_questions_farmer_name_que'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('ans_id', models.IntegerField(primary_key=True, serialize=False)),
                ('que_id', models.IntegerField()),
                ('farmer_id_ans', models.IntegerField()),
                ('ans_body', models.CharField(max_length=500)),
                ('ans_date', models.DateField()),
                ('farmer_name_ans', models.CharField(default='Amritpal Singh', max_length=50)),
            ],
        ),
    ]