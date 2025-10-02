import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,database=name,user=user,password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook where deprecated is null")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                if row[4] != "" and row[5] != "" and row[6] != "":
                    all_phones = row[4] + '\n' + row[5] + '\n' + row[6]
                else:
                    all_phones = ""
                if row[7] != "" and row[8] != "" and row[9] != "":
                    all_emails = row[7] + '\n' + row[8] + '\n' + row[9]
                else:
                    all_emails = ""
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    address=address, all_phones_from_db=all_phones, all_emails_from_homepage=all_emails))
        finally:
            cursor.close()
            return list