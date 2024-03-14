from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from app_resume.models import (
  Profile,
  Experience,
  Skill,
  Education,
)


User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile

class SkillInline(admin.StackedInline):
    model = Skill
    extra = 0


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0


class UserAdmin(DjangoUserAdmin):
    inlines = [ProfileInline, EducationInline, ExperienceInline, SkillInline]
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        normal_user_fieldset = (
            (None, {"fields": ("username", "password")}),
            (_("Personal info"), {"fields": (
                ("first_name", "last_name"),
            "email")}),
        )
        return fieldsets if request.user.is_superuser else normal_user_fieldset
    

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(id=request.user.id)



admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# admin.site.register(Profile)
# admin.site.register(Experience)
# admin.site.register(Skill)
# admin.site.register(Education)