from django.conf import settings
from django.forms.boundfield import BoundField
from django.template.loader import render_to_string


class MultiValueBoundField(BoundField):
    def _subfield_as_widget(self, sub_bf):
        pass

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        pass
