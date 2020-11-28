#! /usr/bin/python3
# coding:utf8

from . import home


@home.route("/")
def index():
    return 'Hi this is home page'
