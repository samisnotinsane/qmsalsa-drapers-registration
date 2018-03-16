from django import forms

from .models import Guest

AMOUNT_CHOICES = (
    (5, ("5 GBP")),
    (3, ("3 GBP"))
)

class GuestForm(forms.ModelForm):
    is_new_to_salsa = forms.BooleanField(label="Beginner?", required=False)
    amount_paid = forms.ChoiceField(choices=AMOUNT_CHOICES, label="Amount")

    class Meta:
        model = Guest
        fields = ['first_name', 
        'last_name', 'email', 'instagram',
        'is_new_to_salsa', 'amount_paid', ]