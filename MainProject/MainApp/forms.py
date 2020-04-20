from django import forms
from django.contrib.auth import get_user_model
from MainApp import views

User = get_user_model()
class ContactForm(forms.Form):

    fullname = forms.CharField(
                widget=forms.TextInput(
                        attrs={

                            "class":"form-control",
                            "placeholder":"fullname"
                        }
                    )
                )
    email = forms.EmailField(
                widget=forms.EmailInput(
                        attrs={

                            "class":"form-control",
                            "placeholder":"Your Email"
                        }
                    )
                )
    content = forms.CharField(
                widget=forms.Textarea(
                        attrs={

                            "class":"form-control",
                            "placeholder":"Your content"
                        }
                    )
                )



    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be a gmail.com")

        return email







class LoginForm(forms.Form):

    username = forms.CharField(
                widget=forms.TextInput(
                        attrs={

                            "class":"form-control",
                            "placeholder":"username"
                        }
                    )
                )


    password = forms.CharField(
                widget=forms.PasswordInput(
                        attrs={

                            "class":"form-control",
                            "placeholder":"password"
                        }
                    )
                )






class RegisterForm(forms.Form):

    username = forms.CharField(
                widget=forms.TextInput(
                        attrs={

                            "class":"form-control",
                            "placeholder":"fullname"
                        }
                    )
                )
    email = forms.EmailField(
                widget=forms.EmailInput(
                        attrs={

                            "class":"form-control",
                            "placeholder":"Email"
                        }
                    )
                )
    password = forms.CharField(
                widget=forms.PasswordInput(
                        attrs={

                            "class":"form-control",
                            "placeholder":"Password"
                        }
                    )
                )


    verify_password = forms.CharField(
                widget=forms.PasswordInput(
                        attrs={

                            "class":"form-control",
                            "placeholder":"Confirm Password"
                        }
                    )
                )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("User already exist")

        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(username=email)
        if email_qs.exists():
            raise forms.ValidationError("User with this email exist")

        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        verify_password = self.cleaned_data.get('verify_password')

        if password != verify_password:
            raise forms.ValidationError("Password do not match")

        return data
