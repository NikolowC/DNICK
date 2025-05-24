from django import forms
from cake_shop.models import Cake


class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = [
            "name",
            "price",
            "weight",
            "description",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super(CakeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
