import json

from django import forms
from django.utils.html import format_html
from .forms import HTMLField
from django.conf import settings


class FormBuilderWidget(forms.Textarea):
    template_name = "dynamic_forms/widgets/formbuilder.html"

    def get_context(self, name, value, attrs):
        pass

    def format_value(self, value):
        pass


class FormRenderWidget(forms.MultiWidget):
    template_name = "dynamic_forms/widgets/formrender.html"

    def decompress(self, value):
        pass


class HTMLFieldWidget(HTMLField):
    def __init__(self, attrs=None, params={}):
        self.attrs = attrs
        self.params = params
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        pass

    def get(self):
        return False

    def use_required_attribute(self, initial):
        pass

    def id_for_label(self, id):
        pass

    def get_context(self):
        pass

    def value_from_datadict(self, data, files, name):
        pass
