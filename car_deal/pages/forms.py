from django import forms


class ContactForm(forms.Form):
    """Custom Form for user contact page"""

    fullname = forms.CharField(
        max_length=100,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
        error_messages={
            "required": "Name Can not be empty",
            "max_length": "Please Enter a Shorter Name"
        }
    )
    email = forms.EmailField(
        max_length=100,
        min_length=3,
        required=True,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email Address', 'class': 'form-control'}
        )
    )
    subject = forms.CharField(
        max_length=200,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Subject', 'class': 'form-control'}),
        error_messages={
            "required": "Subject Can not be empty",
            "max_length": "Please Enter a Shorter Subject"
        }
    )
    phone = forms.CharField(
        max_length=14,
        min_length=11,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
        error_messages={
            "max_length": "Please Enter a valid Cell Phone number",
            "min_length": "Please Enter a valid Cell Phone number"
        }
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'placeholder': 'Enter Your Message Here', 'class': 'form-control'}),
        error_messages={
            "required": "Message Can not be empty",
        }
    )
