import json

from arch import Core, Unit


class Architecture:
    arch_name: str

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
