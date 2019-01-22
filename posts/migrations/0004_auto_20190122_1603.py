# Generated by Django 2.1.5 on 2019-01-22 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20190122_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='內容')),
                ('creat_at', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='更新時間')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator', to=settings.AUTH_USER_MODEL, verbose_name='建立者')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_commits', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL, verbose_name='文章')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
