# Generated by Django 4.1.1 on 2022-10-07 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ZoneSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='zs_fk2', to='dataset.country')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='zs_fk', to='dataset.courier')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='zs_fk3', to='dataset.zone')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sp_fk', to='dataset.courier')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DOX', 'DOX'), ('WPX', 'WPX')], default='DOX', max_length=20)),
                ('price', models.FloatField(max_length=15)),
                ('agent_price', models.FloatField(max_length=15)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='p_fk', to='dataset.courier')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='p_fk2', to='dataset.serviceprovider')),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='p_fk3', to='dataset.weight')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='p_fk4', to='dataset.weight')),
            ],
        ),
        migrations.CreateModel(
            name='CommissionSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_charge', models.FloatField(max_length=15)),
                ('first_commission', models.FloatField(max_length=15)),
                ('second_commission', models.FloatField(max_length=15)),
                ('other', models.FloatField(max_length=15)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cs_fk', to='dataset.courier')),
            ],
        ),
    ]
