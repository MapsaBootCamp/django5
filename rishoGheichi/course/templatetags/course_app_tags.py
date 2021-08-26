import re

from django import template

register = template.Library()


@register.filter(safe=True)
def rial_be_toman(value):
    value = str(int(int(value) / 10))[::-1]
    len_value = len(value)
    res = []
    counter = 0
    for i in range(len_value):
        counter += 1
        if not counter % 3:
            res.append(value[:3][::-1])
            value = value[3:]
            print(value)
    if value:
        res.append(value[::-1])

    return ",".join(res[::-1])


@register.filter(safe=True)
def intcommma(value):
    org = str(value)

    new = re.sub(r"(-?\d+)(\d{3})", r'\g<1>,\g<2>', org)

    if org == new:
        return new
    else:
        return intcommma(new)


@register.inclusion_tag("course/tree_course_category.html")
def tree_structure(course_cat_object):
    subs = course_cat_object.child_cat.all()
    return {"subs": subs}


@register.simple_tag
def find_django(value=None):
    if value:
        return f"hooray {value}"
    return "hooray Django"
