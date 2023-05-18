from atexit import register
from django import template

register = template.Library()
@register.filter(name='has_group')
def has_group(user, group_name):
    grupo = user.groups.filter(name__exact=group_name).exists()
    return grupo


@register.filter(name='group_id') 
def group_id(user, idgroup):
    grupo = user.groups.filter(id__exact=idgroup).exists() 
    # print(grupo)
    return grupo