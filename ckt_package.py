from spice_parser import SubCktParser
from spice_elements import SubCktDecl


class CircuitPackage:
    name: str
    terminals: list(str)

    spice_inst: SubCktDecl
    spice_subckts: list(SubCktDecl)

    gds_inst: object

    def load_spice_ckt(self, path: str, target: str):
        parser = SubCktParser(path).get_subs()
        for i in parser:
            if i.name == target:
                self.spice_inst = i
            else:
                self.spice_subckts.append(i)
