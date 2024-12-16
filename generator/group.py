import random
import string
import os.path
import jsonpickle
import getopt
import sys


from model.group import Group

# парометризация генератора
try:
    opts, arge = getopt.getopt(sys.argv[1:], "n:f:", ["numder of groups", "file"])
    # n - количество данных f - файл
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        n = a


def ramdom_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix+"".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


testdata = [Group(name="", header="", footer="")] + [
    Group(name=ramdom_string("name", 10), header=ramdom_string("header", 20), footer=ramdom_string("footer", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)# определить путь к создаваемому файлу json:
# найти путь к текущему файлу и прибавить к ему хвостик, поднявшись на одну директорию


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
    # положить преобразованную в словарь testdata в файл json
