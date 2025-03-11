from django import forms
from .models import Website


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input mt-1 block w-full",
                    "placeholder": "Enter website name",
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if Website.objects.filter(name=name).exists():
            raise forms.ValidationError("A website with this name already exists.")
        return name
