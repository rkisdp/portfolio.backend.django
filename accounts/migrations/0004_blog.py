# Generated by Django 3.2.7 on 2021-10-06 09:02

import accounts.models.blog
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_verificationtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Instance marked deleted')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Instance marked Active')),
                ('title', models.CharField(help_text='Title of the blog', max_length=64, verbose_name='Title')),
                ('image', models.ImageField(upload_to=accounts.models.blog.upload_to, verbose_name='Image')),
                ('text', models.TextField(verbose_name='Text')),
                ('extra_data', models.JSONField(blank=True, default=dict, help_text='Pass more information here in extra data', verbose_name='Extra Data')),
                ('author', models.ForeignKey(blank=True, help_text='Author of the blog', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_author', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]