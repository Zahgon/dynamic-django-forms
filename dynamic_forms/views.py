from django.views.generic.edit import FormMixin


class DynamicFormMixin(FormMixin):
    form_field = "form"
    form_pk_url_kwarg = "pk"

    response_form_fk_field = None
    response_field = "response"

    def _get_object_containing_form(self, pk):
        pass

    def get_form(self, *args, **kwargs):
        pass

    def form_valid(self, form):
        pass
