# Generated by Django 4.2 on 2023-04-30 13:57

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(unique=True, verbose_name='URL')),
                ('text', models.TextField(verbose_name='Текст ссылки')),
                ('page', models.TextField(verbose_name='Страница, на которой ссылка была встречена')),
                ('visited', models.BooleanField(default=False, verbose_name='Посещалась')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись создана')),
                ('spyder_name', models.TextField(default='spyder_1', verbose_name='Имя паука')),
                ('debug', models.TextField(blank=True, null=True, verbose_name='Ссылка в изначальном виде')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
                'db_table': 'search_links',
                'ordering': ['url'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(unique=True, verbose_name='URL')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('keywords', models.TextField(verbose_name='Ключевые слова')),
                ('status_code', models.IntegerField(default=500, verbose_name='Status Code')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись создана')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись обновлена')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'db_table': 'search_pages',
                'ordering': ['url'],
            },
        ),
        migrations.CreateModel(
            name='SiteCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(unique=True, verbose_name='Domain URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'search_site_categories',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='SitesQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(unique=True, verbose_name='Domain URL')),
                ('visited', models.BooleanField(default=False, verbose_name='Посещался')),
                ('spyder_name', models.TextField(blank=True, default=None, null=True, verbose_name='Имя паука')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись создана')),
            ],
            options={
                'verbose_name': 'Домен',
                'verbose_name_plural': 'Очередь на индексацию',
                'db_table': 'search_sites_queue',
                'ordering': ['url'],
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(unique=True, verbose_name='Word')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись создана')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
                'db_table': 'search_words',
                'ordering': ['word'],
            },
        ),
        migrations.CreateModel(
            name='WordsInPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись создана')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Слова на странице',
                'verbose_name_plural': 'Слова на страницах',
                'db_table': 'search_words_in_pages',
                'ordering': ['page'],
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(unique=True, verbose_name='URL сайта')),
                ('integration_hash', models.TextField(unique=True, verbose_name='Хэш для интеграции метрики')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись создана')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='search.sitecategory', verbose_name='Категория сайта')),
            ],
            options={
                'verbose_name': 'Сайт',
                'verbose_name_plural': 'Все известные сайты',
                'db_table': 'search_sites',
                'ordering': ['url'],
            },
        ),
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(unique=True, verbose_name='Search query')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись создана')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search.page', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Поисковой запрос',
                'verbose_name_plural': 'Поисковые запросы',
                'db_table': 'search_query',
                'ordering': ['query'],
            },
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.site', verbose_name='Сайт страницы'),
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_hash', models.TextField(verbose_name='Хэш пользователя')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись создана')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Запись обновлена')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.site', verbose_name='Сайт страницы')),
            ],
            options={
                'verbose_name': 'Метрика сайта',
                'verbose_name_plural': 'Метрики сайтов',
                'db_table': 'search_metric',
                'ordering': ['site'],
            },
        ),
    ]
