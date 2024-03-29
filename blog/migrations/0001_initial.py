# Generated by Django 2.1.2 on 2018-12-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('author', models.CharField(default='codingkai', max_length=20, verbose_name='作者')),
                ('body', models.TextField(verbose_name='正文')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('read_nums', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('is_public', models.BooleanField(default=True, verbose_name='是否公开')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='标签'),
        ),
    ]
