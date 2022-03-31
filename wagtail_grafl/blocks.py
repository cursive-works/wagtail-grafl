import json
import uuid
import copy

from django import forms
from django.core.exceptions import ValidationError

from wagtail.core import blocks

from .config import WAGTAIL_GRAFL_PLOT_DEFAULTS
from .utils import dict_merge
from .widgets import JSONWidget


class JsonBlock(blocks.FieldBlock):
    """
    JSON field block
    """
    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, validators=(), **kwargs):
        self.field = forms.CharField(
            widget=JSONWidget,
            required=required,
            help_text=help_text,
            max_length=max_length,
            min_length=min_length,
            validators=validators,
        )
        super().__init__(**kwargs)

    def clean(self, value):
        try:
            json.loads(value)
        except json.decoder.JSONDecodeError as e:
            raise ValidationError(f'Invalid JSON: {e}')
        return super().clean(value)


class BaseGraflBlock(blocks.StructBlock):
    """
    Base grafl block class. Classes inhetiting from this should provide a
    get_grafl_data method that returns a dict of grafl compatible data.

    The grafl data is merged with settings WAGTAIL_GRAFL_PLOT_DEFAULTS data
    to allow the developer define a base set of parameters for all plots.

    Data returned from get_grafl_data will override parameters defined in
    WAGTAIL_GRAFL_PLOT_DEFAULTS.
    """
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['value']['uuid'] = uuid.uuid4().hex

        # Get the grafl data and merge it with any defaults
        grafl_data = self.get_grafl_data(value)

        if isinstance(grafl_data, dict):
            context['value']['data'] = dict_merge(
                grafl_data,
                copy.deepcopy(WAGTAIL_GRAFL_PLOT_DEFAULTS),
            )
        return context

    def get_grafl_data(self, value):
        """
        This method should return a dict of grafl data
        """
        raise NotImplementedError('Subclasses should implement this')

    class Meta:
        template = "wagtail_grafl/blocks/grafl.html"


class GraflBlock(BaseGraflBlock):
    """
    Basic grafl block that provides a user ediable JSON field for plot data
    """
    grafl_data = JsonBlock()

    def get_grafl_data(self, value):
        """
        Return a dict of grafl data from a user ediable JSON block
        """
        return json.loads(value['grafl_data'])
