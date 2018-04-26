from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def convert_report_value(context, value, counter):
    return mark_safe(context["conversion_functions"][counter](value))
