import datetime
from collections.abc import Iterable


def to_dict(obj, *filter):
    dic = {}
    for colums in obj._meta.get_fields():
        if colums.name not in filter:
            value = getattr(obj, colums.name, None)
            if not value:
                continue
            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
            dic[colums.name] = value
    return dic


def to_dic_list(obj, *filter):
    rest = []
    if isinstance(obj, Iterable):
        for _obj in iter(obj):
            rest.append(to_dict(_obj, *filter))
    return rest
