from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('publisher', 'company_name', 'title', 'job_type', 'location', 'description', 'post_until',
                  'is_active', 'apply_link')

        widgets = {
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'currentUser',
                                                'type': 'hidden'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'post_until': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'is_active': forms. CheckboxInput(attrs={'class': 'form-check-input'}),
            'apply_link': forms.URLInput(attrs={'class': 'form-control'})
        }
