import random
import string
import os.path
import json
import getopt
import sys


from model.contact import Contact

# парометризация генератора
try:
    opts, arge = getopt.getopt(sys.argv[1:], "n:f:", ["numder of contact", "file"])
    # n - количество данных f - файл
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/data_contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        n = a


def ramdom_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix+"".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


def ramdom_numd(prefix, maxlen):
    symbols = string.digits
    return prefix+"".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


testdata = [
    Contact(first_name="", last_name="", address="", phone_m="", phone_home="", phone_work="",
            email="", email2="", email3="")] + \
           [
    Contact(first_name=ramdom_string("name", 10),
            last_name=ramdom_string("last_name", 10),
            address=ramdom_string("address", 10),
            phone_m=ramdom_numd("", 10),
            phone_home=ramdom_numd("", 10),
            phone_work=ramdom_numd("", 10),
            email=ramdom_string("email", 10),
            email2=ramdom_string("email2", 10),
            email3=ramdom_string("email3", 10),
            )
               for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)# определить путь к создаваемому файлу json:
# найти путь к текущему файлу и прибавить к ему хвостик, поднявшись на одну директорию


with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    # положить преобразованную в словарь testdata в файл json
