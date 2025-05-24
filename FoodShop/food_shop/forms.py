from django import forms

from .models import FoodProduct


class FoodProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoodProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = FoodProduct
        fields = "__all__"
