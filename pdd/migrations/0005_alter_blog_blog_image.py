# Generated by Django 3.2 on 2023-02-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdd', '0004_blog_blognamber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/blog'),
        ),
    ]
