from django.contrib import admin
from app_test.models import (
    Activity,
    Post,
    Question,
    Answer,
    Comment,
)

admin.site.register(Activity)
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)