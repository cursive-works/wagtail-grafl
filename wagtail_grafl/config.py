from django.conf import settings

#
# Default grafl plot settings that can be defined for all plots in settings WAGTAIL_GRAFL_PLOT_DEFAULTS
#

GRAFL_PLOT_DEFAULTS = {
    "figure": {
        "plots": [],
        "layout": {
            "height": 600,
        },
        "update_traces": {},
    },
    "format": {},
}

WAGTAIL_GRAFL_PLOT_DEFAULTS = getattr(settings, "WAGTAIL_GRAFL_PLOT_DEFAULTS", GRAFL_PLOT_DEFAULTS)
