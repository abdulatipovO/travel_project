# Generated by Django 4.0.4 on 2022-07-07 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_news_text_en_news_text_ru_news_text_uz_news_title_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]
