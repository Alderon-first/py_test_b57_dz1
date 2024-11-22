import random
import string

from model.group import Group


const = [
    Group(name="name", header="header", footer="header"),
    Group(name="name1", header="header1", footer="header1")
]


def ramdom_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix+"".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


testdata = [
    Group(name="", header="", footer="")] + \
           [
    Group(name=ramdom_string("name", 10), header=ramdom_string("header", 20), footer=ramdom_string("footer", 20))
               for i in range(5)
]


# вариант тестдаты с перебором комбинаций
# testdata = [
#     Group(name="name", header=header, footer=footer)
#     for name in ["", ramdom_string("name", 10)]
#     for header in ["", ramdom_string("header", 20)]
#     for footer in ["", ramdom_string("footer", 20)]
# ]
