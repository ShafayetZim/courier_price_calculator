from django import forms
from dataset import models


class ContinentCreateForm(forms.ModelForm):
    class Meta:
        model = models.Continent
        fields = (
            'name', 'price')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),

        }


class CountryCreateForm(forms.ModelForm):
    class Meta:
        model = models.Country
        fields = (
            'name', 'code', 'continent')

        def clean_name(self):
            id = self.data['id'] if (self.data['id']).isnumeric() else 0
            name = self.cleaned_data['name']
            try:
                if id > 0:
                    country = models.Country.objects.exclude(id=id).get(name=name)
                else:
                    country = models.Country.objects.get(name=name)
            except:
                return name
            raise forms.ValidationError(f"Country {country.name} already exist")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'continent': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_continent'}
            ),
        }


class WeightCreateForm(forms.ModelForm):
    class Meta:
        model = models.Weight
        fields = (
            'name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ZoneCreateForm(forms.ModelForm):
    class Meta:
        model = models.Zone
        fields = (
            'name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DollarRateForm(forms.ModelForm):
    class Meta:
        model = models.DollarRate
        fields = (
            'rate',)

        widgets = {
            'rate': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CourierCreateForm(forms.ModelForm):
    class Meta:
        model = models.Courier
        fields = (
            'name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ServiceProviderCreateForm(forms.ModelForm):
    class Meta:
        model = models.ServiceProvider
        fields = (
            'name', 'courier')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'courier': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_courier'}
            ),

        }


class PricingCreateForm(forms.ModelForm):
    class Meta:
        model = models.Pricing
        fields = (
            'courier', 'service', 'weight', 'zone', 'type', 'price', 'agent_price')

        widgets = {
            'courier': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_courier'}
            ),
            'service': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_service'}
            ),
            'weight': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_weight'}
            ),
            'zone': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_zone'}
            ),
            'type': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_type'}
            ),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_price': forms.TextInput(attrs={'class': 'form-control'}),

        }


class CommissionSettingCreateForm(forms.ModelForm):
    class Meta:
        model = models.CommissionSetting
        fields = (
            'courier', 'fuel_charge', 'first_commission', 'second_commission', 'other', )

        widgets = {
            'courier': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_courier'}
            ),
            'fuel_charge': forms.TextInput(attrs={'class': 'form-control'}),
            'first_commission': forms.TextInput(attrs={'class': 'form-control'}),
            'second_commission': forms.TextInput(attrs={'class': 'form-control'}),
            'other': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ZoneSettingCreateForm(forms.ModelForm):
    class Meta:
        model = models.ZoneSetting
        fields = (
            'courier', 'country', 'zone', )

        widgets = {
            'courier': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_courier'}
            ),
            'country': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_country'}
            ),
            'zone': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_zone'}
            ),

        }
