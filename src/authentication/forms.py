from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')

class UpdateProfilePictureForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateProfilePictureForm, self).__init__(*args, **kwargs)
        self.fields['profile_photo'].widget.attrs.update({
            'onchange': "preview();"
        })
        #self.fields['profile_photo'].widget.initial_text = 'Current'
        #self.fields['profile_photo'].widget.input_text = 'Select photo'

    class Meta:
        model = get_user_model()
        fields = ('profile_photo',)
