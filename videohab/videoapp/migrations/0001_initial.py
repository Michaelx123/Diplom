# Generated by Django 4.1.1 on 2022-10-02 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clips_name', models.TextField()),
                ('clips_comment', models.TextField()),
                ('clips_hashtag', models.TextField()),
                ('clips_date_create', models.DateTimeField(auto_now_add=True)),
                ('clips_file', models.FileField(blank=True, null=True, upload_to='clips')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('comments_date_create', models.DateTimeField(auto_now_add=True)),
                ('comments_date_update', models.DateTimeField(auto_now_add=True)),
                ('clips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.clips')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_name', models.TextField()),
                ('users_phone', models.TextField(unique=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_for_subscribe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_for_subscribe', to='videoapp.users')),
                ('user_owner_subscribe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_owner_subscribe', to='videoapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='CommentsLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_point', models.SmallIntegerField(default=0)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.comments')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.users')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.users'),
        ),
        migrations.CreateModel(
            name='ClipsLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clips_point', models.SmallIntegerField(default=0)),
                ('clips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.clips')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='BlackLists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blacklist_comment', models.TextField()),
                ('user_in_blacklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_in_blacklist', to='videoapp.users')),
                ('user_owner_blacklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_owner_blacklist', to='videoapp.users')),
            ],
        ),
    ]
