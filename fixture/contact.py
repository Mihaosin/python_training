from model.contact import Contact

class ContactHelper():

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("/html/body/div/div[4]/form[2]/div[1]/input")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[3]/td[8]/a/img").click()
        self.fill_contact(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []

            for element in wd.find_elements_by_name('entry'):
                id = element.find_element_by_name('selected[]').get_attribute("value")
                firstname_text = element.find_element_by_css_selector('td:nth-child(3)').text
                lastname_text = element.find_element_by_css_selector('td:nth-child(2)').text
                self.contact_cache.append(Contact(firstname=firstname_text, lastname=lastname_text, id=id))
        return list(self.contact_cache)