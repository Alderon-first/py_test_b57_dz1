import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self,host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list =[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(name=name, header=header, footer=footer, id=str(id)))
        finally:
            cursor.close()
        return group_list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, address, home, mobile, work, email, email2, email3 "
                           "FROM addressbook")
            for row in cursor:
                (id, firstname, lastname, address, homephone, mobile, work, email, email2, email3 ) = row
                contact_list.append(Contact(id=str(id), first_name=firstname, last_name=lastname, address=address,
                                            phone_home=homephone, phone_m=mobile, phone_work=work,
                                            email=email, email2=email2, email3=email3))
                # print(contact_list)
        finally:
            cursor.close()
        return contact_list
