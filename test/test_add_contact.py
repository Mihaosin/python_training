# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="qwerty", lastname="qwerty", address="Chicago", mobile="987654321"))
