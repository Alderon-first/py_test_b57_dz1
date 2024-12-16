import random
import string

from model.contact import Contact

testdata = [
    Contact(first_name="name",
            last_name="last_name",
            address="address",
            phone_m="",
            phone_home="",
            phone_work="",
            email="email@test1.ru",
            email2="email2@test1.ru",
            email3="email3@test1.ru",
            ),
    Contact(first_name="name1",
            last_name="last_name1",
            address="address1",
            phone_m="1234",
            phone_home="4321",
            phone_work="7879",
            email="email@test.ru",
            email2="email2@test.ru",
            email3="email3@test.ru",
            )
]
