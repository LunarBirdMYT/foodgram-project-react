# Generated by Django 2.2.16 on 2023-03-26 11:29

from django.db import migrations, models
import tags.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название тега', max_length=200, verbose_name='Название тега')),
                ('color', models.CharField(help_text='Цвет для тега', max_length=7, validators=[tags.validators.validate_color], verbose_name='Цвет для тега')),
                ('slug', models.SlugField(help_text='Идентификатор тега', unique=True, verbose_name='Идентификатор тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
    ]
