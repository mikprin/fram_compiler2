import json

from arch_unit import Core, Unit


class Architecture:

    top: list[Unit]
    bottom: list[Unit]
    right: list[Unit]
    left: list[Unit]
    central: Core

    def __init__(self, filename: str, word_size: int, num_words: int):
        try:
            fp = open(filename, 'r')
        except FileNotFoundError:
            print("Specified arch file not found")
            exit()
        arch = json.load(fp)
        self.central = Core(arch, word_size, num_words)
        self.top = [Unit(x) for x in arch['top']]
        self.bottom = [Unit(x) for x in arch['bottom']]
        self.left = [Unit(x) for x in arch['left']]
        self.right = [Unit(x) for x in arch['right']]
        self.import_ckt_packages()

    def import_ckt_packages(self):
        for i in range(len(self.top)):
            self.top[i].create_cp()
        for i in range(len(self.bottom)):
            self.bottom[i].create_cp()
        for i in range(len(self.left)):
            self.left[i].create_cp()
        for i in range(len(self.right)):
            self.right[i].create_cp()
        self.central.create_cp()

    def print_data(self) -> str:
        arch_config = "Architecture:\nCentral:\n"
        if self.central != None: arch_config += self.central.print_unit_config() + "\n"
        if self.top != None:
            arch_config += "Top:\n"
            for i in self.top:
                arch_config += i.print_unit_config()
        if self.bottom != None:
            arch_config += "\n\nBottom:\n"
            for i in self.bottom:
                arch_config += i.print_unit_config()
        if self.left != None:
            arch_config += "\n\nLeft:\n"
            for i in self.left:
                arch_config += i.print_unit_config()
        if self.right != None:
            arch_config += "\n\nRight:\n"
            for i in self.right:
                arch_config += i.print_unit_config()
        arch_config += "\n\n"
        return arch_config

    def evaluate_core_lines(self, h: int, v: int) -> list:
        connections = []
        for i in range(v):
            w_connections = []
            for j in range(h):
                new_connection = dict()
                for l in self.central.lines:
                    if l.type == Core.LineType.HORIZONTAL:
                        new_connection[l.name] = l.name+'_h_'+str(i)
                    if l.type == Core.LineType.VERTICAL:
                        new_connection[l.name] = l.name+'_v_'+str(j)
                w_connections.append(new_connection)
            connections.append(w_connections)
        return connections
    
    def evaluate_side_lines(self, side: list[Unit], n: int, t: Core.LineType) -> list:
        sub = '?'
        if t == Core.LineType.HORIZONTAL:
            sub = '_h_'
        if t == Core.LineType.VERTICAL:
            sub = '_v_'
        layers = []
        for i in side:
            layer_connections = []
            for j in range(n):
                interlayer_dict = dict()
                interlayer_dict[i.connect_with] = i.connect_to + sub + str(j)
                layer_connections.append(interlayer_dict)
            layers.append(layer_connections)
        return layers
            
