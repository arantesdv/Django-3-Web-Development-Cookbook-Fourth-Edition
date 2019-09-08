# Generated by Django 2.2.4 on 2019-09-07 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myproject.apps.ideas.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=myproject.apps.ideas.models.upload_to, verbose_name='Picture')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_ideas', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('categories', models.ManyToManyField(related_name='category_ideas', to='categories.Category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
            },
        ),
        migrations.CreateModel(
            name='IdeaTranslations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=7, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='ideas.Idea', verbose_name='Idea')),
            ],
            options={
                'verbose_name': 'Idea Translations',
                'verbose_name_plural': 'Idea Translations',
                'ordering': ['language'],
                'unique_together': {('idea', 'language')},
            },
        ),
    ]
