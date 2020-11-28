#! /usr/bin/python3
# coding:utf8

from . import admin


@admin.route("/")
def index():
    return 'Hi this is admin page'
