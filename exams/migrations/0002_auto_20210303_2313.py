# Generated by Django 3.1.7 on 2021-03-03 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='required_score_five',
            field=models.IntegerField(help_text='Процент верни отговори за Много добър (4.50)'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='required_score_four',
            field=models.IntegerField(help_text='Процент верни отговори за Добър (3.50)'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='required_score_six',
            field=models.IntegerField(help_text='Процент верни отговори за Отличен (5.50)'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='required_score_to_pass',
            field=models.IntegerField(help_text='Процент верни отговори за Среден (3)'),
        ),
    ]
