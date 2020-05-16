from django import forms
from .models import Member

class MembersForms(forms.ModelForm):

    emple_id = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': 'type your id'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'first name'}))
    midle_i = forms.CharField(max_length=1, widget=forms.TextInput(attrs={'placeholder': 'midle initial'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'last name'}))
    emails = forms.CharField(max_length=50)
    fun_fac = forms.CharField(required= False, widget=forms.Textarea(attrs={'placeholder': 'type your fun facs'}))

    class Meta:
        model = Member
        fields = [
            'emple_id',
            'first_name',
            'midle_i',
            'last_name',
            'emails',
            'fun_fac'
        ]

    def clean_emails(self, *args, **kwargs):
        emails = self.cleaned_data.get('emails')
        if not emails.endswith('.edu'):
            raise forms.ValidationError('This is not the type of email! please use edu ')
        else:
            return emails

