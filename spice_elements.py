class SubCktDecl():
    name: str
    terminals: slice
    elements: slice

    def __init__(self, name, terminals, elements) -> None:
        self.name = name
        self.terminals = terminals
        self.elements = elements


class NestedElement:
    name: str
    module: str
    terminals: str

    def __init__(self, name, module, terminals) -> None:
        self.name = name
        self.module = module
        self.terminals = terminals


class Mosfet(NestedElement):
    width: int
    length: int

    def __init__(self, name, module, terminals, width, length) -> None:
        super().__init__(name, module, terminals)
        self.width = width
        self.length = length

    def modify_width(self, new_width: int):
        """
        Modifies mosfet width
        """
        self.width = new_width

    def modify_length(self, new_length: int):
        """
        Modifies mosfet length
        """
        self.length = new_length


class NestedSubCkt(NestedElement):
    def __init__(self, name, module, terminals):
        super().__init__(name=name, module=module, terminals=terminals)
