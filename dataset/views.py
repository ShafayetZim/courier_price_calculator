import json
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from dataset import models, forms


from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def tpc_dashboard(request):
    context = {'title': 'Shipment',
               'nav_bar': 'dashboard',
               }
    return render(request, 'dashboard.html', context)


def context_data(request):
    fullpath = request.get_full_path()
    abs_uri = request.build_absolute_uri()
    abs_uri = abs_uri.split(fullpath)[0]
    context = {
        'system_host' : abs_uri,
        'page_name' : '',
        'nav_bar' : '',
        'system_name' : 'Tpc',
        'system_short_name' : 'Tpc',
        'topbar' : True,
        'footer' : True,
    }

    return context


def continent(request):
    context = context_data(request)
    context['title'] = 'Continent'
    context['nav_bar'] = "continent_list"
    context['continents'] = models.Continent.objects.all()
    return render(request, 'continent.html', context)


def new_continent(request):
    template_name = 'new_continent.html'

    if request.method == 'GET':
        print("called GET")
        continent_form = forms.ContinentCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        continent_form = forms.ContinentCreateForm(request.POST)

        if continent_form.is_valid():
            obj = continent_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Continent Added Successfully!')
            return redirect('continent-page')

        else:
            print("Not Valid Create Form")
            print(continent_form.errors)

    return render(request, template_name, {
        'continent_form': continent_form,
        'title': 'New Continent',
        'nav_bar': 'new_continent',
    })


class ContinentUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Continent
    form_class = forms.ContinentCreateForm
    success_url = reverse_lazy('continent-page')
    template_name = 'update_continent.html'
    success_message = "Country was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Continent Information"
        context["nav_bar"] = "continent_list"
        return context


def delete_continent(request, id):
    if request.method == 'GET':
        instance = models.Continent.objects.get(id=id)
        models.Continent.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('continent-page')


def country(request):
    context = context_data(request)
    context['title'] = 'Country'
    context['nav_bar'] = "country_list"
    context['country'] = models.Country.objects.all()
    return render(request, 'country.html', context)


def save_country(request):
    resp = { 'status': 'failed', 'msg' : '' }
    if request.method == 'POST':
        post = request.POST
        if not post['id'] == '':
            country = models.Country.objects.get(id=post['id'])
            form = forms.CountryCreateForm(request.POST, instance=country)
        else:
            form = forms.CountryCreateForm(request.POST)

        if form.is_valid():
            form.save()
            if post['id'] == '':
                messages.success(request, "Country has been saved successfully.")
            else:
                messages.success(request, "Country has been updated successfully.")
            resp['status'] = 'success'
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str('<br/>')
                    resp['msg'] += str(f'[{field.name}] {error}')
    else:
         resp['msg'] = "There's no data sent on the request"

    return HttpResponse(json.dumps(resp), content_type="application/json")


def manage_country(request, pk=None):
    context = context_data(request)
    context['title'] = 'manage_country'
    context['nav_bar'] = 'manage_country'
    context['continents'] = models.Continent.objects.all()
    if pk is None:
        context['country'] = {}
    else:
        context['country'] = models.Country.objects.get(id=pk)

    return render(request, 'manage_country.html', context)


def delete_country(request, id):
    if request.method == 'GET':
        instance = models.Country.objects.get(id=id)
        models.Country.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('country-page')


def weight(request):
    context = context_data(request)
    context['title'] = 'Weight'
    context['nav_bar'] = "weight_list"
    context['weights'] = models.Weight.objects.all()
    return render(request, 'weight.html', context)


def new_weight(request):
    template_name = 'new_weight.html'

    if request.method == 'GET':
        print("called GET")
        weight_form = forms.WeightCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        weight_form = forms.WeightCreateForm(request.POST)

        if weight_form.is_valid():
            obj = weight_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Weight Added Successfully!')
            return redirect('weight-page')

        else:
            print("Not Valid Create Form")
            print(weight_form.errors)

    return render(request, template_name, {
        'weight_form': weight_form,
        'title': 'New Weight',
        'nav_bar': 'new_weight',
    })


class WeightUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Weight
    form_class = forms.WeightCreateForm
    success_url = reverse_lazy('weight-page')
    template_name = 'update_weight.html'
    success_message = "Weight was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Weight Information"
        context["nav_bar"] = "weight_list"
        return context


def delete_weight(request, id):
    if request.method == 'GET':
        instance = models.Weight.objects.get(id=id)
        models.Weight.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('weight-page')


def zone(request):
    context = context_data(request)
    context['title'] = 'Zone'
    context['nav_bar'] = "zone_list"
    context['zones'] = models.Zone.objects.all()
    return render(request, 'zone.html', context)


def new_zone(request):
    template_name = 'new_zone.html'

    if request.method == 'GET':
        print("called GET")
        zone_form = forms.ZoneCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        zone_form = forms.ZoneCreateForm(request.POST)

        if zone_form.is_valid():
            obj = zone_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Zone Added Successfully!')
            return redirect('zone-page')

        else:
            print("Not Valid Create Form")
            print(zone_form.errors)

    return render(request, template_name, {
        'zone_form': zone_form,
        'title': 'New Zone',
        'nav_bar': 'new_zone',
    })


class ZoneUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Zone
    form_class = forms.ZoneCreateForm
    success_url = reverse_lazy('zone-page')
    template_name = 'update_zone.html'
    success_message = "Zone was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Zone Information"
        context["nav_bar"] = "zone_list"
        return context


def delete_zone(request, id):
    if request.method == 'GET':
        instance = models.Zone.objects.get(id=id)
        models.Zone.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('zone-page')


def dollar_rate(request):
    context = context_data(request)
    context['title'] = 'Dollar Rate'
    context['nav_bar'] = "dollar_rate"
    context['rates'] = models.DollarRate.objects.all()
    return render(request, 'dollar_rate.html', context)


class DollarRateUpdateView(SuccessMessageMixin, UpdateView):
    model = models.DollarRate
    form_class = forms.DollarRateForm
    success_url = reverse_lazy('dollar-rate')
    template_name = 'update_dollar_rate.html'
    success_message = "Dollar Rate was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Dollar Rate Amount"
        context["nav_bar"] = "dollar_rate"
        return context


def courier(request):
    context = context_data(request)
    context['title'] = 'Courier'
    context['nav_bar'] = "courier_list"
    context['couriers'] = models.Courier.objects.all()
    return render(request, 'courier.html', context)


def new_courier(request):
    template_name = 'new_courier.html'

    if request.method == 'GET':
        print("called GET")
        courier_form = forms.CourierCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        courier_form = forms.CourierCreateForm(request.POST)

        if courier_form.is_valid():
            obj = courier_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Courier Added Successfully!')
            return redirect('courier-page')

        else:
            print("Not Valid Create Form")
            print(courier_form.errors)

    return render(request, template_name, {
        'courier_form': courier_form,
        'title': 'New Courier',
        'nav_bar': 'new_courier',
    })


class CourierUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Courier
    form_class = forms.CourierCreateForm
    success_url = reverse_lazy('courier-page')
    template_name = 'update_courier.html'
    success_message = "Courier was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Courier Information"
        context["nav_bar"] = "courier_list"
        return context


def delete_courier(request, id):
    if request.method == 'GET':
        instance = models.Courier.objects.get(id=id)
        models.Courier.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('courier-page')


def service_provider(request):
    context = context_data(request)
    context['title'] = 'Service Provider'
    context['nav_bar'] = "service_provider_list"
    context['services'] = models.ServiceProvider.objects.all()
    return render(request, 'service_provider.html', context)


def new_service_provider(request):
    template_name = 'new_service_provider.html'

    if request.method == 'GET':
        print("called GET")
        service_form = forms.ServiceProviderCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        service_form = forms.ServiceProviderCreateForm(request.POST)

        if service_form.is_valid():
            obj = service_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Service Provider Added Successfully!')
            return redirect('service-provider-page')

        else:
            print("Not Valid Create Form")
            print(service_form.errors)

    return render(request, template_name, {
        'service_form': service_form,
        'title': 'New Service Provider',
        'nav_bar': 'new_service_provider',
    })


class ServiceProviderUpdateView(SuccessMessageMixin, UpdateView):
    model = models.ServiceProvider
    form_class = forms.ServiceProviderCreateForm
    success_url = reverse_lazy('service-provider-page')
    template_name = 'update_service_provider.html'
    success_message = "Service Provider was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Service Provider Information"
        context["nav_bar"] = "service_provider_list"
        return context


def delete_service_provider(request, id):
    if request.method == 'GET':
        instance = models.ServiceProvider.objects.get(id=id)
        models.ServiceProvider.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('service-provider-page')


def pricing(request):
    context = context_data(request)
    context['title'] = 'Pricing'
    context['nav_bar'] = "pricing_list"
    context['pricing'] = models.Pricing.objects.all()
    return render(request, 'pricing.html', context)


def new_pricing(request):
    template_name = 'new_pricing.html'

    if request.method == 'GET':
        print("called GET")
        pricing_form = forms.PricingCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        pricing_form = forms.PricingCreateForm(request.POST)

        if pricing_form.is_valid():
            obj = pricing_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Pricing Added Successfully!')
            return redirect('pricing-page')

        else:
            print("Not Valid Create Form")
            print(pricing_form.errors)

    return render(request, template_name, {
        'pricing_form': pricing_form,
        'title': 'New Pricing',
        'nav_bar': 'new_pricing',
    })


class PricingUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Pricing
    form_class = forms.PricingCreateForm
    success_url = reverse_lazy('pricing-page')
    template_name = 'update_pricing.html'
    success_message = "Pricing was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Pricing Information"
        context["nav_bar"] = "pricing_list"
        return context


def delete_pricing(request, id):
    if request.method == 'GET':
        instance = models.Pricing.objects.get(id=id)
        models.Pricing.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('pricing-page')


def commission_setting(request):
    context = context_data(request)
    context['title'] = 'Commission Setting'
    context['nav_bar'] = "commission_setting_list"
    context['commissions'] = models.CommissionSetting.objects.all()
    return render(request, 'commission_setting.html', context)


def dhl_commission_setting(request):
    context = context_data(request)
    context['title'] = 'Commission Setting'
    context['nav_bar'] = "dhl_commission_setting_list"
    context['commissions'] = models.CommissionSetting.objects.filter(courier='3').all()
    return render(request, 'commission_setting.html', context)


def upc_commission_setting(request):
    context = context_data(request)
    context['title'] = 'Commission Setting'
    context['nav_bar'] = "upc_commission_setting_list"
    context['commissions'] = models.CommissionSetting.objects.filter(courier='2').all()
    return render(request, 'commission_setting.html', context)


def tpc_commission_setting(request):
    context = context_data(request)
    context['title'] = 'Commission Setting'
    context['nav_bar'] = "tpc_commission_setting_list"
    context['commissions'] = models.CommissionSetting.objects.filter(courier='1').all()
    return render(request, 'commission_setting.html', context)


def new_commission_setting(request):
    template_name = 'new_commission_setting.html'

    if request.method == 'GET':
        print("called GET")
        commission_form = forms.CommissionSettingCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        commission_form = forms.CommissionSettingCreateForm(request.POST)

        if commission_form.is_valid():
            obj = commission_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Commission Setting Added Successfully!')
            return redirect('commission-setting-page')

        else:
            print("Not Valid Create Form")
            print(commission_form.errors)

    return render(request, template_name, {
        'commission_form': commission_form,
        'title': 'New Commission Setting',
        'nav_bar': 'new_commission_setting',
    })


class CommissionSettingUpdateView(SuccessMessageMixin, UpdateView):
    model = models.CommissionSetting
    form_class = forms.CommissionSettingCreateForm
    success_url = reverse_lazy('commission_setting-page')
    template_name = 'update_commission_setting.html'
    success_message = "Commission Setting was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Commission Setting Information"
        context["nav_bar"] = "commission_setting_list"
        return context


def delete_commission_setting(request, id):
    if request.method == 'GET':
        instance = models.CommissionSetting.objects.get(id=id)
        models.CommissionSetting.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('commission-setting-page')


def zone_setting(request):
    context = context_data(request)
    context['title'] = 'Zone Setting'
    context['nav_bar'] = "zone_setting_list"
    context['zones'] = models.ZoneSetting.objects.all()
    return render(request, 'zone_setting.html', context)


def dhl_zone_setting(request):
    context = context_data(request)
    context['title'] = 'Zone Setting'
    context['nav_bar'] = "dhl_zone_setting_list"
    context['zones'] = models.ZoneSetting.objects.filter(courier=3).all()
    return render(request, 'zone_setting.html', context)


def upc_zone_setting(request):
    context = context_data(request)
    context['title'] = 'Zone Setting'
    context['nav_bar'] = "upc_zone_setting_list"
    context['zones'] = models.ZoneSetting.objects.filter(courier=2).all()
    return render(request, 'zone_setting.html', context)


def tpc_zone_setting(request):
    context = context_data(request)
    context['title'] = 'Zone Setting'
    context['nav_bar'] = "tpc_zone_setting_list"
    context['zones'] = models.ZoneSetting.objects.filter(courier=1).all()
    return render(request, 'zone_setting.html', context)


def new_zone_setting(request):
    template_name = 'new_zone_setting.html'

    if request.method == 'GET':
        print("called GET")
        zone_form = forms.ZoneSettingCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        zone_form = forms.ZoneSettingCreateForm(request.POST)

        if zone_form.is_valid():
            obj = zone_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Zone setting Added Successfully!')
            return redirect('zone-setting-page')

        else:
            print("Not Valid Create Form")
            print(zone_form.errors)

    return render(request, template_name, {
        'zone_form': zone_form,
        'title': 'New Zone Setting',
        'nav_bar': 'new_zone_setting',
    })


class ZoneSettingUpdateView(SuccessMessageMixin, UpdateView):
    model = models.ZoneSetting
    form_class = forms.ZoneSettingCreateForm
    success_url = reverse_lazy('zone-setting-page')
    template_name = 'update_zone_setting.html'
    success_message = "Zone Setting was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Zone Setting Information"
        context["nav_bar"] = "zone_setting_list"
        return context


def delete_zone_setting(request, id):
    if request.method == 'GET':
        instance = models.ZoneSetting.objects.get(id=id)
        models.ZoneSetting.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('zone-setting-page')


def index(request):
    context = context_data(request)
    context['title'] = 'index'
    context['nav_bar'] = "index"
    context['index'] = models.Continent.objects.all()
    return render(request, 'web/index.html', context)
