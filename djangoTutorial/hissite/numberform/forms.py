from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)

'''
class InputForm(forms.Form):

    test_number = forms.IntegerField(help_text = "Enter 6 digit test number")
'''

from .models import TestNumberModel

class InputNumberForm(forms.ModelForm):
    class Meta:
        model = TestNumberModel
        #fields = "__all__"
        fields = [
            "test_number",
            "test_number_one",
            "test_number_two",
        ]