from arch import Core, Unit
import json

class Architecture:
    top: list
    bottom: list
    right: list
    left: list
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
