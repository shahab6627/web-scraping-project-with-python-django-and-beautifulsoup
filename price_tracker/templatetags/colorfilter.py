from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter
def colorfilter(val):
    el = str(val)[:1]
    if el == '-':
        color = f'<b style="color:green">{val} -> price goes down</b>'
    elif el == "0":
        color = f'<span>{val}</span>'
    else:
        color = f'<b style="color:red">{val} -> price goes up</b>'
    return mark_safe(color)
        
        
        
        
    