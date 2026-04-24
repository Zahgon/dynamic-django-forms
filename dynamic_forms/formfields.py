from django import forms
from .boundfields import MultiValueBoundField
from .widgets import FormBuilderWidget, FormRenderWidget
from .utils import gen_fields_from_json


class FormBuilderField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = FormBuilderWidget
        return super().__init__(*args, **kwargs)


class FormRenderField(forms.MultiValueField):
    def __init__(self, form_json=[], required=False, **kwargs):
        kwargs['error_messages'] = {
            'incomplete': 'Please fill in all required fields.',
        }
        kwargs['fields'] = gen_fields_from_json(form_json)
        kwargs['label'] = ""
        kwargs['require_all_fields'] = False
        kwargs['required'] = required
        del kwargs['max_length']
        super().__init__(**kwargs)
        self.configure_widget()

    def get_bound_field(self, form, field_name):
        pass

    def configure_widget(self):
        pass

    def _configure_new_fields(self, fields):
        pass

    def add_fields(self, form_json):
        pass

    def replace_fields(self, form_json):
        pass

    def compress(self, data):
        pass
