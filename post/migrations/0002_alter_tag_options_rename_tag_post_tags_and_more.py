# Generated by Django 4.0.5 on 2022-06-04 20:07

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=10000, verbose_name='Caption'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to=post.models.user_directory_path, verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=75, verbose_name='Tag'),
        ),
    ]
