# Generated by Django 4.2.5 on 2023-11-10 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import userauths.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('visibility', models.CharField(choices=[('Only Me', 'Only Me'), ('Everyone', 'Everyone')], default='everyone', max_length=10)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz123', length=7, max_length=25, prefix='')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Post',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.post')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
                'ordering': ['-date'],
            },
        ),
    ]
