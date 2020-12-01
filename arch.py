from os import name
from sys import exec_prefix
from typing import Any
import sys


class Core:
    name = ""
    word_size = 1
    num_words = 1

    def __init__(self, core_description: dict, word_size: int, num_words: int) -> None:
        descr = core_description['central']
        self.name = descr['cell']
        self.word_size = word_size
        self.num_words = num_words


class Unit:
    name = ""
    mirror = False
    connect_to = ""
    connect_with = ""
    special_type = ""
    other = dict()

    def __init__(self, unit_description: Any) -> None:
        self.name = unit_description['unit']
        try: self.connect_to = unit_description['to']
        except KeyError:
            print("Error: child connection for unit "+self.name+" not specified. Please check arch file.")
            sys.exit(1)
        try: self.connect_with = unit_description['with']
        except KeyError:
            print("Error: parent connection for unit "+self.name+" not specified. Please check arch file.")
            sys.exit(1)
        self.mirror = unit_description.get('other').get('mirror')
        self.special_type = unit_description.get('other').get('special_type')
        other = unit_description.get('other_connections')
        if other != None:
            self.other = self.setup_other_connections(other)

    def setup_other_connections(self, other_connections: dict) -> dict:
        return {x: OptionalConnection(other_connections[x]) for x in other_connections}

class OptionalConnection:
    name = ""
    type = ""
    point = ""
    def __init__(self, connection) -> None:
        self.name = connection['name']
        self.type = connection['type']
        if self.type == 'common':
            self.point = connection['common_net']
        if self.type == 'bus_connection':
            self.point = connection['common_bus']
