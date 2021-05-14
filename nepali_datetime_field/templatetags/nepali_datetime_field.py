from django import template

register = template.Library()


@register.filter
def nepali_date(value):
    if isinstance(value, str):
        return value
    return value.strftime("%K-%n-%D")
