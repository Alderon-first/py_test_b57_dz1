class Contact:
    #класс Contact - это конструктов объекта "контакт"
    def __init__(self, first_name=None, last_name=None, address=None, phone_m=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_m = phone_m
        self.email = email

