# Wagtail-Grafl

Create charts in Wagtail streamfields using the [Grafl.io](https://grafl.io/) plotting service.

## Installation

Install from [PyPI](https://pypi.org/project/wagtail-grafl/):

```
pip install wagtail-grafl
```

Then add the following to your project's `INSTALLED_APPS`.

```
'wagtail_grafl',
```

## Out of the box

There are currently three blocks available in `wagtail-grafl`.

### GraflBlock

The primary block used for creating basic Grafl plots.

It consists of a single JSON field for entering Grafl plot data. It inherits from `BaseGraflBlock`.

### JsonBlock

Simple formatted JSON field with basic validation and included in `GraflBlock`.

### BaseGraflBlock

The `BaseGraflBlock` is provided to make it easy to extend `wagtail-grafl` and build your own bespoke Grafl blocks.

It provides the `get_grafl_data` method that needs to be overridden in any blocks that inherit from this.

The `get_grafl_data` method should return a dictionary of Grafl compatible data.

This make it possible for custom blocks to pull in data from other sources and generate Grafl plots programatically.

### Settings

* WAGTAIL_GRAFL_PLOT_DEFAULTS - a optional dictionary of default parameters that is merged with the blocks grafl data. This is useful for specifying parameters that should be consistent across all Grafl plot blocks.

### Example use

Add the StreamBlock to a StreamField on a Wagtail page:

```
from wagtail import blocks
from wagtail_grafl.blocks import GraflBlock

class MyStreamBlock(blocks.StreamBlock):
    grafl_plot = GraflBlock()
```

Add the `StreamBlock` to a `StreamField` on a Wagtail page:

```
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from .blocks import MyStreamBlock


class MyPage(Page):

    body = StreamField(MyStreamBlock(), null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
```

Then in the page template:

```
{% load static wagtailcore_tags %}

{% include_block page.body %}
```

## About Grafl

Grafl is a plotting service that can be used to generate plots from basic JSON data. It's based on Plotly, free to use and very flexible.
