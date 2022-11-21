from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.tpc_dashboard, name="calc-dashboard"),
    path('continent', views.continent, name='continent-page'),
    path('new_continent', views.new_continent, name="new-continent"),
    path('update_continent/<int:pk>', views.ContinentUpdateView.as_view(), name='update-continent'),
    path('delete_continent/<int:id>', views.delete_continent, name="delete-continent"),

    path('country', views.country, name='country-page'),
    path('manage_country',views.manage_country,name='manage-country'),
    path('manage_country/<int:pk>',views.manage_country,name='manage-country-pk'),
    path('delete_country/<int:id>',views.delete_country,name='delete-country'),
    path('save_country',views.save_country,name='save-country'),

    path('weight', views.weight, name='weight-page'),
    path('new_weight', views.new_weight, name="new-weight"),
    path('update_weight/<int:pk>', views.WeightUpdateView.as_view(), name='update-weight'),
    path('delete_weight/<int:id>', views.delete_weight, name="delete-weight"),

    path('zone', views.zone, name='zone-page'),
    path('new_zone', views.new_zone, name='new-zone'),
    path('update_zone/<int:pk>', views.ZoneUpdateView.as_view(), name='update-zone'),
    path('delete_zone/<int:id>', views.delete_zone, name='delete-zone'),

    path('courier', views.courier, name='courier-page'),
    path('new_courier', views.new_courier, name='new-courier'),
    path('update_courier/<int:pk>', views.CourierUpdateView.as_view(), name='update-courier'),
    path('delete_courier/<int:id>', views.delete_courier, name='delete-courier'),

    path('service_provider', views.service_provider, name='service-provider-page'),
    path('new_service_provider', views.new_service_provider, name='new-service-provider'),
    path('update_service_provider/<int:pk>', views.ServiceProviderUpdateView.as_view(), name='update-service-provider'),
    path('delete_service_provider/<int:id>', views.delete_service_provider, name='delete-service-provider'),

    path('dollar_rate', views.dollar_rate, name='dollar-rate'),
    path('update_dollar_rate/<int:pk>', views.DollarRateUpdateView.as_view(), name='update-dollar-rate'),

    # path('commission_setting', views.commission_setting, name='commission-setting-page'),
    path('dhl_commission_setting', views.dhl_commission_setting, name='dhl-commission-setting-page'),
    path('upc_commission_setting', views.upc_commission_setting, name='upc-commission-setting-page'),

    path('new_commission_setting', views.new_commission_setting, name='new-commission-setting'),
    path('update_commission_setting/<int:pk>', views.CommissionSettingUpdateView.as_view(), name='update-commission-setting'),
    path('delete_commission_setting/<int:id>', views.delete_commission_setting, name='delete-commission-setting'),

    path('zone_setting', views.zone_setting, name='zone-setting-page'),
    path('new_zone_setting', views.new_zone_setting, name='new-zone-setting'),
    path('update_zone_setting/<int:pk>', views.ZoneSettingUpdateView.as_view(), name='update-zone-setting'),
    path('delete_zone_setting/<int:id>', views.delete_zone_setting, name='delete-zone-setting'),

    path('pricing', views.pricing, name='pricing-page'),
    path('new_pricing', views.new_pricing, name='new-pricing'),
    path('update_pricing/<int:pk>', views.PricingUpdateView.as_view(), name='update-pricing'),
    path('delete_pricing/<int:id>', views.delete_pricing, name='delete-pricing'),

]