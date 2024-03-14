from django import forms


class ProfileForm(forms.Form):
    about_me = forms.CharField(
        label="About Me",
        max_length=1000,
        # help_text="Write something about yourself",
        widget=forms.Textarea(
            attrs={
                "rows":"5",
                "class": "form-control",
                'placeholder': "Write something about yourself"
                }
            )
        )


class SocialLinksForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if 'initial' in kwargs:
            if kwargs['initial']['facebook'] == None:
                kwargs['initial']['facebook'] = ''
            if kwargs['initial']['twitter'] == None:
                kwargs['initial']['twitter'] = ''
            if kwargs['initial']['google_plus'] == None:
                kwargs['initial']['google_plus'] = ''
            if kwargs['initial']['linkedin'] == None:
                kwargs['initial']['linkedin'] = ''
            if kwargs['initial']['github'] == None:
                kwargs['initial']['github'] = ''
        super().__init__(*args, **kwargs)

    facebook = forms.URLField(
        max_length=70,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    twitter = forms.URLField(
        max_length=70,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    google_plus = forms.URLField(
        max_length=70,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    linkedin = forms.URLField(
        max_length=70,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    github = forms.URLField(
        max_length=70,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class ExperienceForm(forms.Form):
    title = forms.CharField(
        max_length=70,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        max_length=400,
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows":"5",
        })
    )
    employer = forms.CharField(
        max_length=70,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    employee_start_date = forms.DateField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "date"
            }
        )
    )
    employee_end_date = forms.DateField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "date"
            },
        )
    )