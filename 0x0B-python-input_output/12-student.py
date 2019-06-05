#!/usr/bin/python3
class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs != None:
            dict1 = {}
            for key, val in self.__dict__.items():
                for key2 in attrs:
                    if key2 == key:
                        dict1.update({key: val})
            return dict1
        else:
            return self.__dict__
