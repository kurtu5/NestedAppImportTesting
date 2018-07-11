# -*- coding: utf-8 -*-
name = 'baseclass'
class BaseClass(object):
    def __init__(self, arg):
        print(f'Base class initializing as {__class__} with arg={arg}')
