from django import forms
from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.project_models.Category import Category


class ModelAttributeForm(forms.Form):
    MODEL_CHOICES = [
        ("Project", "Project"),
        ("Category", "Category"),
    ]

    model = forms.ChoiceField(choices=MODEL_CHOICES, label="Model")
    attributes = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label="Attributes",
    )

    def set_attributes_choices(self, model_name):
        if model_name == "Project":
            self.fields["attributes"].choices = [
                (field.name, field.name) for field in Project._meta.get_fields()
            ]
        elif model_name == "Category":
            self.fields["attributes"].choices = [
                (field.name, field.name) for field in Category._meta.get_fields()
            ]
