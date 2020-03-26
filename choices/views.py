from .models import Choice
import json


def get_json(field):
    new_lst = []
    obj = {}
    q = Choice.objects.filter(field=field)
    for c in q:
        new_lst.append({'value': c.code, 'text': c.text})
        obj['data'] = new_lst
        j = json.dumps(new_lst)
    return j


def get_tuple(field):
    return Choice.objects.filter(field=field).values_list('code', 'text')
