from ckt_package import CircuitPackage

class CompiledSpice:

    subckt_list: list[dict]

    def __init__(self) -> None:
        self.subckt_list = list()
        self.subckt_library = set()
        pass

    def add_subckt(self, subckt: CircuitPackage, connection_dict: dict[str, str]):
        new_block = dict()
        new_block["ckt"] = subckt
        new_block['cn'] = connection_dict
        self.subckt_list.append(new_block)
    
    def build(self):
        decls = set()
        result: str = ''
        #Unite subckt sets
        for i in range(len(self.subckt_list)):
            decls.union(self.subckt_list[i]['ckt'].spice_subckts)
            decls.add(self.subckt_list[i]['ckt'].spice_inst)
        #Declaring all used subckts
        for d in decls:
            result += d.declare()
        #Instanciating all ckts
        for i in range(len(self.subckt_list)):
            ckt = self.subckt_list[i]['ckt']
            result += ckt.instantiate(self.subckt_list[i]['cn'], instance_index=i)
        return result