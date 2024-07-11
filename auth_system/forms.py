from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('bio', 'profile_picture')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'bio': forms.Textarea(attrs={'class': 'form-control'}),
        # }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['bio'].widget.attrs.update({'class': 'form-control'})

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'