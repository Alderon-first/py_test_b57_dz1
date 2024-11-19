from sys import maxsize


class Group:
    # класс Contact - это конструктов объекта "группа"
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s: %s; %s; %s" % (self.id, self.name, self.header, self.footer)
        # переопределение вывода на консоль

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.name == other.name
        # переопределение функции сравнения
        # id сравнивается без учета None

    def id_or_max(self):
        # определение функции определения числовного значения id группы, если id отсутствует.
        # для целей сортировки групп в списке: определение положения группы в списке. группа без id будет считаться
        # гуппой с самым большим числовым значением id
        if self.id:
            return int(self.id)
        else:
            return maxsize

