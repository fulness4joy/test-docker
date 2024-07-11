from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.title}"


class UserPoll(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    title = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()


class Choice(models.Model):
    user_poll = models.ForeignKey(UserPoll, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_check = models.BooleanField(default=False)