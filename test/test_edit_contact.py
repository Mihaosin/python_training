# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="asdfasdfas", lastname="asdfafsd", address="Saint-petersburg",  mobile="987654321"))
    app.session.logout()
