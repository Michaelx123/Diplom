from django.db import models
from django.contrib.auth.models import User


class Users (models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    users_name = models.TextField()
    users_phone = models.TextField(unique=True)


class Clips (models.Model):
    clips_name = models.TextField()
    clips_comment = models.TextField()
    clips_hashtag = models.TextField()
    clips_date_create = models.DateTimeField(auto_now_add=True)


class ClipsLikes (models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    clips = models.ForeignKey(Clips, on_delete=models.CASCADE)
    clips_point = models.SmallIntegerField(default=0)  # 1 = Like, -1 = dislike


class Comments (models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    clips = models.ForeignKey(Clips, on_delete=models.CASCADE)
    comments_text = models.TextField()
    comments_date_create = models.DateTimeField(auto_now_add=True)
    comments_date_update = models.DateTimeField(auto_now_add=True)


class CommentsLikes (models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    comments_point = models.SmallIntegerField(default=0)  # 1 = Like, -1 = dislike


class Subscribes (models.Model):
    user_owner_subscribe = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_owner_subscribe')  #Пользователь, чьи это подписки
    user_for_subscribe = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_for_subscribe')  #Авторы клипов, на которые подписан пользователь выше


class BlackLists (models.Model):
    user_owner_blacklist = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_owner_blacklist')  #Пользователь, чей это список
    user_in_blacklist = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_in_blacklist')  #Пользователь, которого забанили
    blacklist_comment = models.TextField()  #Можно заполнить комментарий за что внесен конкретный пользователь в черный список
