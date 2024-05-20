# Generated by Django 3.2 on 2021-05-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20210507_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='imgUrl',
        ),
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(null=True, upload_to='Portfolio/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
