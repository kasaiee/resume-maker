from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), on_delete=models.CASCADE)
    project_count = models.IntegerField(_('Project Count'), default=0)
    experience_count = models.IntegerField(default=0)
    position = models.CharField(max_length=50, help_text=_('Current position at the company or project you are working now'))
    title = models.CharField(max_length=50, help_text=_('Enter your job title'))
    phone_number = models.CharField(max_length=12)
    about_me = models.TextField(null=True, max_length=10000)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    google_plus = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=50)
    description = models.TextField(null=True, max_length=200)
    employer = models.CharField(null=True, max_length=50)
    employee_start_date = models.DateField(null=True)
    employee_end_date = models.DateField(null=True)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=50)
    description = models.TextField(null=True, max_length=200)
    image = models.ImageField(upload_to='skills', null=True)


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=50)
    description = models.TextField(null=True, max_length=200)
    academy_title = models.CharField(null=True, max_length=50)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)