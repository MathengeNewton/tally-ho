from django.db import models
from django_enumfield import enum

from libya_tally.libs.models.base_model import BaseModel
from libya_tally.libs.models.enums.form_state import FormState
from libya_tally.libs.models.enums.gender import Gender


class ResultForm(BaseModel):
    class Meta:
        app_label = 'tally'

    ballot = models.ForeignKey('Ballot', null=True)
    center = models.ForeignKey('Center', null=True)

    barcode = models.PositiveIntegerField(unique=True)
    form_stamped = models.NullBooleanField()
    form_state = enum.EnumField(FormState)
    gender = enum.EnumField(Gender, null=True)
    name = models.CharField(max_length=256, null=True)
    office = models.CharField(max_length=256, null=True)
    serial_number = models.PositiveIntegerField(unique=True)
    station_number = models.PositiveSmallIntegerField(null=True)