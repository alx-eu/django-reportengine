from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def convert_report_value(context, value, counter):
    return context["conversion_functions"][counter](value)
