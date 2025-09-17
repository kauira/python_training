import re
from selenium.webdriver.support.ui import Select
from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contant_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_birthdate_selection("bday", contact.bday)
        self.change_birthdate_selection("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_adate_selection("aday", contact.aday)
        self.change_adate_selection("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def change_adate_selection(self, field_name, option):
        wd = self.app.wd
        if option is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_value(option)
            wd.find_element_by_css_selector(f"select[name=\"{field_name}\"] > option[value=\"{option}\"]").click()

    def change_birthdate_selection(self, field_name, option):
        wd = self.app.wd
        if option is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_value(option)
            wd.find_element_by_xpath(f"//option[@value='{option}']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_add_contant_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select first contant
        wd.find_elements_by_name("selected[]")[index].click()
        # delete first contact
        wd.find_element_by_css_selector("[value='Delete']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        # select all contacts
        wd.find_element_by_css_selector("#MassCB").click()
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_css_selector("[value='Update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_form(self, new_contact_data):
        self.edit_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("[title='Edit']").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("[title='Edit']")[index].click()

    def delete_contact_from_edit_page(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # click on delete button
        wd.find_element_by_css_selector("[value='Delete']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        self.open_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname_text = cells[1].text
                firstname_text = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname_text, firstname=firstname_text, id=id, address=address,
                                                  all_phones_from_homepage = all_phones, all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(lastname=lastname, firstname=firstname, id=id,
                       address=address, home=home, work=work, mobile=mobile,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work)