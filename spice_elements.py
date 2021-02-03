import sys


class SubCktDecl:
    name: str
    terminals: list[str]
    elements: list

    def __init__(self, name, terminals, elements) -> None:
        self.name = name
        self.terminals = terminals
        self.elements = elements
    
    def instantiate(self, connections: dict[str, str], instance_index: int=0) -> str:
        """
        Creates instance string of subcircuit

        Parameters
        ----------
            connections: dict[str, str]
            Connections list styled like: terminal->wire

        Optional
        --------
            instance_index: int
            Instance index for generating names inside parental subcircuit.
            Default value: 0

        Returns
        -------
            str Generated string
        """
        # Making terminals list
        new_terminals: list[str] = []
        for i in self.terminals:
            try:
                new_terminals.append(connections[i])
            except KeyError:
                print("Error: terminal " + str(i) + " connection for subcircuit " + self.name + " not specified")
                sys.exit(-2)
        new_name = "X"+str(instance_index)
        nested_subckt_instance = NestedSubCkt(new_name, self.name, new_terminals)
        return nested_subckt_instance.synthesize_declaration()

    def declare(self) -> str:
        """
        Creates subcircuit declaration

        Returns
        -------
            str Generated declaration text
        """
        hat = ".subckt " + self.name + ' '.join(self.terminals) + "\n"
        for decl in self.elements:
            hat += decl.synthesize_declaration() + "\n"
        hat += ".ends " + self.name
        return hat
    
    def print_decl_info(self) -> str:
        info = "\nSubcircuit name: {}\tTerminals: {}\t Elements:\n".format(self.name, ', '.join(self.terminals))
        for i in self.elements:
            info += i.print_description()
        return info

class NestedElement:
    name: str
    module: str
    terminals: list[str]

    def __init__(self, name: str, module: str, terminals: list[str]) -> None:
        """
        Creates new nested element representation

        Parameters
        ----------
            name: str
            Element instance name
        ----------
            module: str
            Element module name
        ----------
            terminals: list[str]
            List of terminals
        
        Returns
        -------
            None
        """
        super().__init__()
        self.name = name
        self.module = module
        self.terminals = terminals
    
    def synthesize_declaration(self) -> str:
        """
        Synthesizes string with nested element description

        Returns
        -------
            str Syntesized declaration
        """
        synthesized_string: str = self.name+ " ("
        term_len: int = len(self.terminals)
        i: int = 0
        synthesized_string += ' '.join(self.terminals) + ') '
        synthesized_string += self.module
        return synthesized_string
    
    def print_description(self) -> str:
        info = "Name: {}\tModule: {}\tTerminals: {}\t".format(self.name, self.module, ', '.join(self.terminals))
        return info



class Mosfet(NestedElement):
    width: int
    length: int
    fingers_amount: int
    mult: int
    srcefirst: int

    def __init__(self, name: str, module: str, terminals: list[str], width: int, length: int, nfing: int = None, mult: int = None, srcefirst: int = None) -> None:
        super().__init__(name, module, terminals)
        self.width = width
        self.length = length
        self.fingers_amount = nfing
        self.mult = mult
        self.srcefirst = srcefirst

    def modify_width(self, new_width: int) -> None:
        """
        Modifies mosfet width

        Paramters
        ---------
            new_width: int
            New MOSFET width
        
        Returns
        -------
            None
        """
        self.width = new_width

    def modify_length(self, new_length: int) -> None:
        """
        Modifies mosfet length

        Paramters
        ---------
            new_length: int
            New MOSFET length
        
        Returns
        -------
            None
        """
        self.length = new_length
    
    def synthesize_declaration(self) -> str:
        """
        Synthesizes MOSFET declaration

        Returns
        -------
            str Syntesized declaration
        """
        synth_string = super().synthesize_declaration()
        synth_string += ('w=' + str(self.width)+ ' ')
        synth_string += ('l=' + str(self.length))
        if self.fingers_amount != None: synth_string += (' nfing=' + str(self.fingers_amount))
        if self.mult != None: synth_string += (' mult='+str(self.mult))
        if self.srcefirst != None: synth_string += (' srcefirst='+str(self.srcefirst))
        return synth_string
    
    def print_description(self) -> str:
        info = super().print_description()
        info += "Width: {}\tLength: {}\t".format(str(self.width), str(self.length))
        if self.fingers_amount != None: info += ('Fingers: ' + str(self.fingers_amount) + '\t')
        if self.mult != None: info += ('Mult: '+str(self.mult) + '\t')
        if self.srcefirst != None: info += ('Source First: '+str(self.srcefirst) + '\n')
        info += "\n"
        return info


class NestedSubCkt(NestedElement):
    """
    Neseted subcircuit representation
    e.g. X0 (a1 a2 a3 gnd) subckt
    """
    def __init__(self, name: str, module: str, terminals: list[str]) -> None:
        """
        Create new nested subckt

        Parameters
        ----------
            name: str
            Instance name e.g. X0
        ----------
            module: str
            Module name e.g. subckt
        ----------
            terminals: list[str]
            List of terminals in order of their connection
        
        Returns
        -------
            None
        """
        super().__init__(name=name, module=module, terminals=terminals)
    
    def print_description(self) -> str:
        return super().print_description() + "\n"
