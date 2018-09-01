import datetime

from django import forms
from django.utils.html import format_html

import utils


class Html5DateInput(forms.DateInput):
    input_type = 'date'


class AngularPopupDatePicker(forms.DateInput):

    def __init__(self, attrs=None, max=None, min=None):
        if attrs is None:
            attrs = {}
        if max is not None:
            attrs['max-date'] = convert_date(max)
        if min is not None:
            attrs['min-date'] = convert_date(min)

        attrs['datepicker-popup'] = True
        attrs['is-open'] = 'status.{name}'
        attrs['placeholder'] = 'yyyy-MM-dd'
        super(AngularPopupDatePicker, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        input_str = super(AngularPopupDatePicker, self).render(name, value, attrs)
        input_str = format_html(input_str, name=name)
        tmpl_str = '<p class="input-group">{input_str}<span class="input-group-btn">'
        tmpl_str += '<button type="button" class="btn btn-default" ng-click="status.{name} = !status.{name}">'
        tmpl_str += '<i class="glyphicon glyphicon-calendar"></i></button></span>'
        return format_html(tmpl_str, input_str=input_str, name=name)


def convert_date(date_in):
    date = utils.today()
    if hasattr(date_in, 'strftime'):  # Date object
        date = date_in
    elif hasattr(date_in, 'real'):  # number object assume delta days
        date = utils.today() + datetime.timedelta(days=date_in)

    return "'{}'".format(date.strftime('%Y-%m-%d'))
