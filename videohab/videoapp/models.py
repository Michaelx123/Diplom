import time
import requests
from django.db import models
from django.contrib.auth.models import User


class Users (models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    users_name = models.TextField()
    users_phone = models.TextField(unique=True)


class Clips (models.Model):
    clips_name = models.TextField()
    clips_comment = models.TextField()
    clips_date_create = models.DateTimeField(auto_now_add=True)
    clips_file = models.FileField(upload_to='clips/%Y%m%d_%H%M', null=True, blank=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)


class Hashtags (models.Model):
    hashtag_name = models.TextField(unique=True)

    def save(self, *args, **kwargs):  # Все хэштеги сохраняем в нижнем регистре
        self.hashtag_name = self.hashtag_name.lower()
        return super(Hashtags, self).save(*args, **kwargs)


class ClipsHashtags (models.Model):
    clips = models.ForeignKey(Clips, on_delete=models.CASCADE)
    hashtags = models.ForeignKey(Hashtags, on_delete=models.CASCADE)


class ClipsLikes (models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    clips = models.ForeignKey(Clips, on_delete=models.CASCADE)
    clips_likes_date = models.DateTimeField(auto_now_add=True) #Поле для аналитики, для основной задачи не особо нужно


class ClipsDislikes (models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    clips = models.ForeignKey(Clips, on_delete=models.CASCADE)
    clips_dislikes_date = models.DateTimeField(auto_now_add=True) #Поле для аналитики, для основной задачи не особо нужно


class Comments (models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    clips = models.ForeignKey(Clips, on_delete=models.CASCADE)
    comments_text = models.TextField()
    comments_date_create = models.DateTimeField(auto_now_add=True)
    comments_date_update = models.DateTimeField(auto_now_add=True)


class CommentsLikes (models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    comments_likes_date = models.DateTimeField(auto_now_add=True)


class CommentsDislikes (models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    comments_dislikes_date = models.DateTimeField(auto_now_add=True)


class Subscribes (models.Model):
    user_owner_subscribe = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_owner_subscribe')  #Пользователь, владелец подписки
    user_for_subscribe = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_for_subscribe')  #Авторы клипов(канал), на которые подписан пользователь выше
    subscribes_date = models.DateTimeField(auto_now_add=True)


class BlackLists (models.Model):
    user_owner_blacklist = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_owner_blacklist')  #Пользователь, чей это список
    user_in_blacklist = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_in_blacklist')  #Пользователь, которого забанили
    blacklist_comment = models.TextField()  #Можно заполнить комментарий за что внесен конкретный пользователь в черный список
    blacklists_date = models.DateTimeField(auto_now_add=True)
