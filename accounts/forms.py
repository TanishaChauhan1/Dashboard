from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import BlogPost


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'user_type', 'address_line1', 'city', 'state', 'pincode')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password does not match")


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'draft']

    def clean_summary(self):
        summary = self.cleaned_data.get('summary', '')
        # Truncate summary to 15 words if longer
        if len(summary.split()) > 15:
            summary = ' '.join(summary.split()[:15]) + '...'
        return summary
