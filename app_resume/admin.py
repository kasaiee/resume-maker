from django.contrib import admin
from app_resume.models import (
  Profile,
  Experience,
  Skill,
  Education,
)


admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Education)