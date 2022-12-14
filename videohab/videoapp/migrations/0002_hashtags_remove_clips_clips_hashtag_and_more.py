# Generated by Django 4.1.1 on 2022-11-07 17:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag_name', models.TextField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='clips',
            name='clips_hashtag',
        ),
        migrations.RemoveField(
            model_name='clipslikes',
            name='clips_point',
        ),
        migrations.RemoveField(
            model_name='commentslikes',
            name='comments_point',
        ),
        migrations.AddField(
            model_name='blacklists',
            name='blacklists_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clipslikes',
            name='clips_likes_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentslikes',
            name='comments_likes_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscribes',
            name='subscribes_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clips',
            name='clips_file',
            field=models.FileField(blank=True, null=True, upload_to='clips/%Y%m%d_%H%M'),
        ),
        migrations.CreateModel(
            name='CommentsDislikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_dislikes_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.comments')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='ClipsHashtags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.clips')),
                ('hashtags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.hashtags')),
            ],
        ),
        migrations.CreateModel(
            name='ClipsDislikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clips_dislikes_date', models.DateTimeField(auto_now_add=True)),
                ('clips', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.clips')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.users')),
            ],
        ),
    ]
