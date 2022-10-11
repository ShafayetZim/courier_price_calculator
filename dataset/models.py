from django.db import models


class Courier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    courier = models.ForeignKey(Courier, on_delete=models.DO_NOTHING, related_name='sp_fk')

    def __str__(self):
        return self.name


class Weight(models.Model):
    name = models.FloatField(max_length=15)

    def __str__(self):
        return str(self.name)


class Zone(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Continent(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=15)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=200, blank=True, null=True)
    continent = models.ForeignKey(Continent, on_delete=models.DO_NOTHING, )

    def __str__(self):
        return self.name


class Pricing(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.DO_NOTHING, related_name='p_fk')
    service = models.ForeignKey(ServiceProvider, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='p_fk2')
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING, related_name='p_fk3')
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, related_name='p_fk4')
    TYPE_CHOICES = (
        ('DOX', 'DOX'),
        ('WPX', 'WPX'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='DOX')
    price = models.FloatField(max_length=15)
    agent_price = models.FloatField(max_length=15)

    def __str__(self):
        return str(f"{self.courier} - {self.weight}")


class CommissionSetting(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.DO_NOTHING, related_name='cs_fk')
    fuel_charge = models.FloatField(max_length=15)
    first_commission = models.FloatField(max_length=15)
    second_commission = models.FloatField(max_length=15)
    other = models.FloatField(max_length=15)

    def __str__(self):
        return str(self.courier)


class ZoneSetting(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.DO_NOTHING, related_name='zs_fk')
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, related_name='zs_fk2')
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, related_name='zs_fk3')

    def __str__(self):
        return str(self.courier)


class DollarRate(models.Model):
    rate = models.FloatField(max_length=100)

    def __str__(self):
        return str(self.rate)
