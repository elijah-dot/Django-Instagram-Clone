# Generated by Django 4.0.5 on 2022-06-06 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=1000, verbose_name='caption'),
        ),
    ]
