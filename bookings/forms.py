from django.forms import ModelForm

from bookings.models import Guest


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields =['first_name','last_name','email','phone','address','country','check_in','check_out']
