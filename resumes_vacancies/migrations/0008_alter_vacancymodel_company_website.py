# Generated by Django 3.2.7 on 2021-10-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes_vacancies', '0007_auto_20211013_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancymodel',
            name='company_website',
            field=models.TextField(blank=True, verbose_name='Посилання на сайт компанії'),
        ),
    ]
