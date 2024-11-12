from sys import maxsize


class Contact:
    #класс Contact - это конструктов объекта "контакт"
    def __init__(self, first_name=None, last_name=None, address=None, phone_m=None, email=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_m = phone_m
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s: %s %s" % (self.id, self.first_name, self.last_name)
        # переопределение вывода на консоль

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.first_name == other.first_name \
               and self.last_name == other.last_name
        # переопределение функции сравнения
        # id сравнивается без учета None

    def id_or_max(self):
        # определение функции определения числовного значения id контакта, если id отсутствует.
        # для целей сортировки контактов в списке: определение положения группы в списке. контакт без id будет считаться
        # контактом с самым большим числовым значением id
        if self.id:
            return int(self.id)
        else:
            return maxsize
