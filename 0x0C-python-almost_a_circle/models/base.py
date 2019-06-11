#!/usr/bin/python3
import json
import csv


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == "":
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_ob2 = []
        if list_objs is not None:
            for i in list_objs:
                list_ob2.append(i.to_dictionary())
        with open('{}.json'.format(cls.__name__), 'w') as File:
            File.write(cls.to_json_string(list_ob2))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            panda_dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            panda_dummy = cls(1)
        panda_dummy.update(**dictionary)
        return panda_dummy

    @classmethod
    def load_from_file(cls):
        list_obj2 = []
        try:
            with open('{}.json'.format(cls.__name__), 'r') as File:
                File2 = cls.from_json_string(File.read())
                for i in File2:
                    list_obj2.append(cls.create(**i))
        except:
            pass
        return list_obj2

    @classmethod
    def save_to_file_csv(cls, list_objs):
        for a in list_objs:
            dict_1 = a.to_dictionary()
        with open(cls.__name__ + ".csv", 'w') as mycsv:
            keys = dict_1.keys()
            dictw = csv.DictWriter(mycsv, keys)
            dictw.writeheader()
            for a in list_objs:
                dictw.writerow(a.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        list_ob_csv = []
        with open(cls.__name__ + ".csv", 'r') as mycsv:
            dictr = csv.DictReader(mycsv)
            for row in dictr:
                for key, value in row.items():
                    row[key] = int(value)
                list_ob_csv.append(cls.create(**row))
        return list_ob_csv
