from django import forms

from .models import Flight


class FlightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Flight
        fields = "__all__"
