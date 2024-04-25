from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth.models import User


class Activity(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class Post(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    likes = GenericRelation(Activity)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    activities = GenericRelation(Activity)

    def __str__(self):
        return self.title

class Answer(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    votes = GenericRelation(Activity)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    likes = GenericRelation(Activity)
    def __str__(self):
        return self.title
