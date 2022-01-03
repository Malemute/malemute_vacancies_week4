from django import forms

class PromoCodeForm(forms.Form):
    user = forms.CharField()
    code = forms.CharField(min_length=16, max_length=16)

def add_custom_errors(promo_code_form):
    if promo_code_form.is_valid():
        code_data = promo_code_form.data.get('code')
        if code_data[0:4] != '2022':
            promo_code_form.add_error('code', 'промо-код истек')
        elif code_data[-6:] != 'django':
            promo_code_form.add_error('code', 'контрольная сумма неверна')
