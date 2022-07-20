# Generated by Django 4.0.6 on 2022-07-20 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to='news.category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_caption',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='published_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.region'),
        ),
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='news', to='news.tag'),
        ),
    ]