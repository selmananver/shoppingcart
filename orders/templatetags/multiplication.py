from django import template

register =template.Library()

@register.simple_tag(name='multiplication')

def multiplication(a,b):
   return a * b
  