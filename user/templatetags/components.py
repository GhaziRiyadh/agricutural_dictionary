from django import template
from django.template import loader

register = template.Library()


@register.simple_tag
def show_component(request, component, **kwargs):
    context = {}
    for key, value in kwargs.items():
        context[key] = value
    return loader.get_template(component).render(context, request)
