from django import forms
from django.forms import ModelForm
from .models import Tasks


class TasksForms(ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"
    Task_text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter task...",
            }
        ),
    )

    task_condition = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={"class": "form-check-input"}),
    )
