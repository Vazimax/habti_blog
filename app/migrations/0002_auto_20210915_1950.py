# Generated by Django 3.2.5 on 2021-09-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='brief',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('technology', 'technology'), ('science', 'science'), ('education', 'education'), ('business', 'business'), ('entrepreneurship', 'entrepreneurship')], max_length=100, null=True),
        ),
    ]
