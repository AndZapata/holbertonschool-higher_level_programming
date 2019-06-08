#!/usr/bin/python3
import json


class Base():
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        jason = cls.to_json_string(list_objs)
        print(jason)
        with open('{}.json'.format(cls), 'w') as myFile:
            json.dump(jason, myFile)
