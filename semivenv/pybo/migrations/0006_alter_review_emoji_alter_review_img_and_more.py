# Generated by Django 4.1.2 on 2022-10-11 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_review_viewidx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='emoji',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='img',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='viewIdx',
            field=models.IntegerField(null=True),
        ),
    ]
