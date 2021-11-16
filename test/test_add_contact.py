# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.test_add_contact(Contact(firstname="qwerty", lastname="qwerty", address="Chicago", mobile="987654321"))
    app.session.logout()
