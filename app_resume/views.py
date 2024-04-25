from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_resume.forms import ProfileForm, SocialLinksForm, ExperienceForm
from django.contrib import messages
from django.forms import formset_factory 
from django.core import serializers
from app_resume.helpers import get_form_set_keys, get_form_set_values
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required


def index(request):
    return render(request, 'index.html')

@login_required
def resume(request):
    return render(request, 'resume.html')


@login_required
def templates(request):
    if request.user.has_perm('auth.can_choose_template'):
        return render(request, 'templates.html')
    else:
        raise PermissionDenied("You do not have permission to Enter Clients in Other Company, Be Careful")

@permission_required("auth.can_choose_template", login_url='/403')
def templates(request):
    return render(request, 'templates.html')


@login_required
def edit(request):
    ExperienceFormSet = formset_factory(ExperienceForm, extra=1)
    if request.method == "POST":
        form_set_indexes = get_form_set_keys(request)
        request.user.experience_set.all().delete()
        for key in form_set_indexes:
            experience_data = get_form_set_values(request, key)
            request.user.experience_set.create(**experience_data)
        profile_form = ProfileForm(request.POST)
        social_links_form = SocialLinksForm(request.POST)
        experience_form_set = ExperienceFormSet(request.POST)
        if profile_form.is_valid() and social_links_form.is_valid():
            request.user.profile.about_me = profile_form.cleaned_data['about_me']
            request.user.profile.facebook = request.POST.get('facebook')
            request.user.profile.twitter = request.POST.get('twitter')
            request.user.profile.google_plus = request.POST.get('google_plus')
            request.user.profile.linkedin = request.POST.get('linkedin')
            request.user.profile.github = request.POST.get('github')
            request.user.profile.save()

            messages.add_message(request, messages.SUCCESS, "Saved successfully")
        else:
            messages.add_message(request, messages.ERROR, "Fill the form")
    else:
        profile_form = ProfileForm(initial=request.user.profile.__dict__)
        social_links_form = SocialLinksForm(initial=request.user.profile.__dict__)
        experience_form_set = ExperienceFormSet(
            initial=[ex.__dict__ for ex in request.user.experience_set.all()]
        )
        ex = request.user.experience_set.first()
        data = ex.__dict__ if ex else {}
    
    return render(request, 'edit.html', {
        'profile_form': profile_form,
        'social_links_form': social_links_form,
        'experience_form_set': experience_form_set,
        'experience_set': serializers.serialize('json', request.user.experience_set.all())
    })