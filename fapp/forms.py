from django import forms
from Crowdfunding_platform.models.project_models.Project import Project
from Crowdfunding_platform.models.project_models.Category import Category


class ProjectForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        required=True,
        label="Category",
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'goal_amount', 'category', 'status', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['end_date'].widget = forms.HiddenInput()
