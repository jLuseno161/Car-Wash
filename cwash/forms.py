from crispy_forms.helper import FormHelper
from cwash.models import Booking, Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'profile_pic', 'bio', 'contact']



class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Booking

        widgets = {
            'user': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter Mobile No.'}),
            'email': forms.TextInput(attrs={'placeholder': 'eg: mymail@gmail.com'}),
            'plan': forms.Select(),
            'vehicle_type': forms.Select(),
            'timeframe': forms.Select(),
            'appointment_date': forms.TimeInput(attrs={'placeholder': 'Appointment Date'})
        }
        fields = ('user', 'mobile', 'email', 'plan',
                  'vehicle_type', 'timeframe', 'appointment_date')

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
