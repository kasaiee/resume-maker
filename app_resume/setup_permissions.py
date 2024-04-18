def setup_advanced_user_permissions():
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from django.contrib.auth import get_user_model
    User = get_user_model()
    group, created = Group.objects.get_or_create(name="advanced_user")
    if created:
        profile_content_type = ContentType.objects.get_for_model(User)
        permission, created = Permission.objects.get_or_create(
            codename="can_choose_template",
            content_type_id=profile_content_type.id
        )
        group.permissions.add(permission)