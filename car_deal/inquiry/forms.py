from django import forms

from .models import Inquiry


# This solution is for funtion based view
# class InformForm(forms.Form):
# ...
#    def __init__(self, user=None,*args, **kwargs):
#         super(InformForm, self).__init__(**kwargs)
#         if user:
#             self.fields['somefield'] = forms.ChoiceField()
#             self.fields['somefield'].widget = forms.Select()
#             self.fields['somefield'].queryset = Someobject.objects.filter(User=user)
# ...

class InquiryForm(forms.ModelForm):
    """Define users Car Inquiry Form"""

    def __init__(self, *args, **kwargs):
        """ Grants access to the user object so that logged in users can't
        edit name field"""

        super(InquiryForm, self).__init__(*args, **kwargs)
        # if kwargs["user"]:
        #     self.user = kwargs.pop('user')
        #     self.fields['user'].initial = self.user
        #     self.fields['name'].initial = self.user.username

    class Meta:
        model = Inquiry
        # fields = ['name', 'car', 'customer_query', 'city', 'state', 'email', 'phone', 'comment']
        exclude = ['user', ]
        phone = forms.CharField(min_length=12, max_length=14)

        # Defining input attribute
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'car': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_query': forms.TextInput(attrs={'placeholder': 'Your Query', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
        }

        error_messages = {
            "name": {
                "required": "Name Can not be Empty",
                "max_length": "Please Enter A Shorter Name"
            },
        }
