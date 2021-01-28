from os import name
from guide import Guide
from spice_parser import SubCktParser
from spice_elements import SubCktDecl


class CircuitPackage:
    name: str
    terminals: list[str] = []

    spice_inst: SubCktDecl
    spice_subckts: list[SubCktDecl] = []

    gds_inst: object

    def load_spice_ckt(self, path: str) -> None:
        """
        Loads SPICE file and parses into this package

        Parameters
        ----------
            path: str - path to SPICE file
        """
        parser = SubCktParser(path).get_subs()
        self.spice_subckts = []
        for i in parser:
            if i.name == self.name:
                self.spice_inst = i
                self.terminals = i.terminals
            else:
                self.spice_subckts.append(i)

    def load_gds_ckt(self, path: str) -> None:
        """
        Loads GDS file and parses into this package

        Parameters
        ----------
            path: str - path to GDS file
        """
        pass

    def __init__(self, name: str, loc: str) -> None:
        """
        Creates new package with name name from folder loc
        """
        super().__init__()
        self.name = name
        if loc == None:
            loc = Guide.locate(name)
        self.load_spice_ckt(loc + name + ".sp")
        self.load_gds_ckt(loc + name + ".gds")
    
    def print_pkg_info(self) -> str:
        info = "\nPackage name: {}\tTerminals: {}".format(self.name, self.terminals)
        if hasattr(self, 'spice_inst'): info += "\nMain SPICE subcircuit: " + self.spice_inst.print_decl_info()
        if self.spice_subckts != None:
            info += "\nSPICE cubcircuits:\n"
            for i in self.spice_subckts:
                info += i.print_decl_info()
        return info