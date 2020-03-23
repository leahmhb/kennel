from .choices import COLORS, SEXES, COUNTRIES, STATES
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def get_states(request):
    obj = {}
    new_lst = []
    for s in STATES:
        new_lst.append({'value': s[0], 'text': s[1]})
    obj['data'] = new_lst
    json = JSONRenderer().render(new_lst)
    return HttpResponse(json, content_type='application/json')


def get_countries(request):
    obj = {}
    new_lst = []
    for s in COUNTRIES:
        new_lst.append({'value': s[0], 'text': s[1]})
    obj['data'] = new_lst
    json = JSONRenderer().render(new_lst)
    return HttpResponse(json, content_type='application/json')


def get_sexes(request):
    obj = {}
    new_lst = []
    for s in SEXES:
        new_lst.append({'value': s[0], 'text': s[1]})
    obj['data'] = new_lst
    json = JSONRenderer().render(new_lst)
    return HttpResponse(json, content_type='application/json')


def get_colors(request):
    obj = {}
    new_lst = []
    for s in COLORS:
        new_lst.append({'value': s[0], 'text': s[1]})
    obj['data'] = new_lst
    json = JSONRenderer().render(new_lst)
    return HttpResponse(json, content_type='application/json')
