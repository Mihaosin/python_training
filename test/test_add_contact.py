# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="qwerty", lastname="qwerty", mobile_number="987654321"))
    app.session.logout()

