# Generated by Django 4.2.4 on 2023-09-03 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_balence', models.DecimalField(decimal_places=2, max_digits=10, max_length=20)),
                ('account_number', shortuuid.django_fields.ShortUUIDField(alphabet='4596873525', length=10, max_length=25, prefix='219', unique=True)),
                ('account_id', shortuuid.django_fields.ShortUUIDField(alphabet='4596RETYTOYX', length=7, max_length=25, prefix='MOI', unique=True)),
                ('pin_number', shortuuid.django_fields.ShortUUIDField(alphabet='123456789', length=4, max_length=7, prefix='', unique=True)),
                ('ref_code', shortuuid.django_fields.ShortUUIDField(alphabet='aacgeo4592712', length=5, max_length=7, prefix='', unique=True)),
                ('account_status', models.CharField(choices=[('activate', 'Active'), ('in_active', 'In_active')], default='in_active', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kyc_statue', models.BooleanField(default=False)),
                ('kyc_confirmed', models.BooleanField(default=False)),
                ('recommanded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='account_recommand', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
