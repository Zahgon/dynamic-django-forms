import json

from django.db import models
from .formfields import FormBuilderField, FormRenderField


class FormField(models.TextField):
    """Stores JSON Schema for form
    """

    def from_db_value(self, value, expression, connection):
        pass

    def to_python(self, value):
        pass

    def get_prep_value(self, value):
        pass

    def formfield(self, **kwargs):
        pass


class ResponseField(models.TextField):
    """Stores JSON response to form.
    """

    def from_db_value(self, value, expression, connection):
        pass

    def to_python(self, value):
        pass

    def get_prep_value(self, value):
        pass

    def formfield(self, *args, **kwargs):
        pass
