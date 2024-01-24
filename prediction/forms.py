from django import forms
from .models import CsvUpload, TeamName

class CsvUploadForm(forms.ModelForm):
    class Meta:
        model = CsvUpload
        fields = ['csv_file']





class TeamStatusForm(forms.Form):
    team_name = forms.ModelChoiceField(
        queryset=TeamName.objects.all(),
        empty_label="Select an option"
    )



class CompersionForm(forms.Form):
    team_name = forms.ModelChoiceField(
        queryset=TeamName.objects.all(),
        empty_label="Select an option"
    )

    oponent_name = forms.ModelChoiceField(
        queryset=TeamName.objects.all(),
        empty_label="Select an option"
    )
