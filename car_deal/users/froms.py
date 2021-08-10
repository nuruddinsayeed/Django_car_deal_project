from django import forms

from users.models import CustomUser


class UserRegForm(forms.ModelForm):
    """Djanog Form for Custom User Registration"""

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """Here We setup Our custom Form"""

        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

        # Customize defautl Labels
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'Email': 'Email Address',
            'password': 'Password'
        }

        # Defining password input
        widgets = {
            'password': forms.PasswordInput(),
            'Email': forms.EmailInput()
        }

        error_messages = {
            "username": {
                "required": "Name Can not be Empty",
                "max_length": "Please Enter A Shorter Name"
            },

        }

    # Overriding clean funciton to add client site pass check validation
    def clean(self):
        cleaned_data = super(CustomUser, self).clean
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
