import sys
from enum import Enum

from ckt_package import CircuitPackage


class ArchUnit:
    name: str
    pkg: CircuitPackage

    def create_cp(self) -> None:
        """
        Creates circuit package for this unit
        """
        self.pkg = CircuitPackage(self.name, None)
    
    def print_unit_config(self) -> str:
        config = "Name: {0}".format(self.name)
        config += self.pkg.print_pkg_info()
        return config


class Core(ArchUnit):
    word_size: int = 1
    num_words: int = 1
    lines: list[str] = []

    def __init__(self, core_description: dict, word_size: int, num_words: int) -> None:
        """
        Creates core with specified parameters

        Parameters
        ----------
        core_description: dict
            Core description from architecture specification
        ----------
        word_size: int
            Word length
        ----------
        num_words: int
            Amount of words
        """
        descr = core_description['central']
        self.name = descr['cell']
        self.word_size = word_size
        self.num_words = num_words
        self.lines = descr["lines"]

    class LineType(Enum):
        VERTICAL = 1
        HORIZONTAL = 2

    class CoreLine:
        name = ""
        type = 0

        def __init__(self, line: dict) -> None:
            self.name = line["name"]
            if line["type"] == 'horizontal':
                self.type = self.LineType.HORIZONTAL
            elif line["type"] == 'vertical':
                self.type = self.LineType.VERTICAL
            else:
                print("Unknown line type in " +
                      self.name + " inside central cell")
                sys.exit(1)

    def setup_lines(self, lines: slice) -> slice:
        return [self.CoreLine(x) for x in lines]

    def print_unit_config(self) -> str:
        info = super().print_unit_config()
        info += "Word size: "+str(self.word_size) + "\t"
        info += "Amount of words: "+str(self.num_words) + "\t"
        info += "Lines: \n"
        for i in self.lines:
            for j in i:
                info += j + " : " + i[j]+"\n"
        return info



class Unit(ArchUnit):
    mirror = False
    connect_to = ""
    connect_with = ""
    special_type = ""
    other = dict()

    def __init__(self, unit_description: dict) -> None:
        self.name = unit_description['unit']
        try:
            self.connect_to = unit_description['to']
        except KeyError:
            print("Error: child pin connection for unit " +
                  self.name+" not specified. Please check arch file.")
            sys.exit(-1)
        try:
            self.connect_with = unit_description['with']
        except KeyError:
            print("Error: parent connection pin for unit " +
                  self.name+" not specified. Please check arch file.")
            sys.exit(-1)
        self.mirror = unit_description.get('other').get('mirror')
        self.special_type = unit_description.get('other').get('special_type')
        other = unit_description.get('array_interconnections')
        if other != None:
            self.other = self.setup_other_connections(other)

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

    def setup_other_connections(self, other_connections: dict) -> dict:
        return {x: self.OptionalConnection(other_connections[x]) for x in other_connections}
