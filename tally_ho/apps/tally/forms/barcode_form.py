from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator,\
    RegexValidator
from django.utils.translation import ugettext as _

from tally_ho.apps.tally.models.result_form import ResultForm
from tally_ho.apps.tally.models.station import Station


disable_copy_input = {
    'onCopy': 'return false;',
    'onDrag': 'return false;',
    'onDrop': 'return false;',
    'onPaste': 'return false;',
    'autocomplete': 'off',
    'class': 'form-control'
}

barcode_scan_input_attributes = disable_copy_input.copy()
barcode_scan_input_attributes.update({'id': 'id_scanned_barcode'})


class BarcodeForm(forms.Form):
    error_messages = {'invalid': _(u"Expecting only numbers for barcodes")}
    validators = [
        MaxLengthValidator(255),
        MinLengthValidator(1),
        RegexValidator(
            regex=r'^[0-9]*$',
            message=_(u"Expecting only numbers for barcodes")
        ),
    ]

    barcode = forms.CharField(
        error_messages=error_messages,
        validators=validators,
        required=False,
        widget=forms.NumberInput(
            attrs=disable_copy_input))
    barcode_copy = forms.CharField(
        error_messages=error_messages,
        validators=validators,
        required=False,
        widget=forms.NumberInput(
            attrs=disable_copy_input))
    barcode_scan = forms.CharField(
        error_messages=error_messages,
        validators=validators,
        required=False,
        widget=forms.NumberInput(
            attrs=barcode_scan_input_attributes))

    tally_id = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(BarcodeForm, self).__init__(*args, **kwargs)
        self.fields['barcode'].widget.attrs['autofocus'] = 'on'
        self.fields['barcode_scan'].widget.attrs['autofocus'] = 'on'

    def clean(self):
        """Verify that barcode and barcode copy match and that the barcode is
        for a result form in the system.

        Also checks if the center,station and/or races are enabled.
        """
        if self.is_valid():
            cleaned_data = super(BarcodeForm, self).clean()
            barcode_scan = cleaned_data.get('barcode_scan')
            barcode = cleaned_data.get('barcode')
            barcode_copy = cleaned_data.get('barcode_copy')
            tally_id = cleaned_data.get('tally_id')

            if not barcode_scan and barcode != barcode_copy:
                raise forms.ValidationError(_(u"Barcodes do not match!"))

            try:
                result_form = ResultForm.objects.get(
                    barcode=barcode or barcode_scan,
                    tally__id=tally_id)
            except ResultForm.DoesNotExist:
                raise forms.ValidationError(_(u"Barcode does not exist."))
            else:
                if result_form.center and not result_form.center.active:
                    raise forms.ValidationError(_(u"Center is disabled."))
                elif result_form.station_number:
                    try:
                        station = Station.objects.get(
                            station_number=result_form.station_number,
                            center=result_form.center)
                    except Station.DoesNotExist:
                        raise forms.ValidationError(
                            _(u"Station does not exist."))
                    else:
                        if not station.active:
                            raise forms.ValidationError(
                                _(u"Station disabled."))
                        elif station.sub_constituency:
                            ballot = station.sub_constituency.get_ballot()
                            if ballot and not ballot.active:
                                raise forms.ValidationError(
                                    _(u"Race disabled."))

            return cleaned_data
