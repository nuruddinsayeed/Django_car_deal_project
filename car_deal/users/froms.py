from django import forms

from users.models import CustomUser


class UserRegForm(forms.ModelForm):
    """Djanog Form for Custom User Registration"""

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

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
            'username': forms.TextInput(attrs={'placeholder': 'UserName', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
        }

        error_messages = {
            "username": {
                "required": "Name Can not be Empty",
                "max_length": "Please Enter A Shorter Name"
            },

        }

    # Overriding clean funciton to add client site pass check validation
    def clean(self):
        cleaned_data = super(UserRegForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Passwords doesn't match")
            # raise forms.ValidationError(
            #     "Password and Confirm Password does not match"
            # )


class LoginForm(forms.Form):
    """Create django login form"""

    username = forms.CharField(
        max_length=150,
        label="Username",
        required=True,
        error_messages={
            "required": "Name Can not be empty",
            "max_length": "Please Enter a Shorter Name"
        },
        widget=forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'form-control'}),
    )

    password = forms.CharField(
        max_length=255,
        label="Password",
        required=True,
        error_messages={
            "required": "Password Can not be empty",
            "max_length": "Please Enter a Shorter Password"
        },
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
