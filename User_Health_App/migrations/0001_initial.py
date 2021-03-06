# Generated by Django 3.0.7 on 2020-11-07 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHealthInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=2)),
                ('blood_group', models.CharField(max_length=100)),
                ('genotype', models.CharField(max_length=100)),
                ('ebola_status', models.BooleanField(help_text='Do you have ebola currently?')),
                ('malaria_status', models.BooleanField(help_text='Do you have malaria currently?')),
                ('previous', models.BooleanField(help_text='Do you have previous health challenges?')),
                ('previous_illness1', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_illness2', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_illness3', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_illness4', models.CharField(blank=True, max_length=100, null=True)),
                ('previous_illness5', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(max_length=300, on_delete=django.db.models.deletion.CASCADE, related_name='client_health', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
