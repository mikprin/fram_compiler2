from enum import IntFlag
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
                print("Warning: terminal " + str(i) + " connection for subcircuit " + self.name + " not specified. Passing default terminal")
                new_terminals.append(i)
        new_name = str(instance_index)
        nested_subckt_instance = NestedSubCkt(new_name, self.name, new_terminals)
        return nested_subckt_instance.synthesize_declaration()

    def declare(self) -> str:
        """
        Creates subcircuit declaration

        Returns
        -------
            str Generated declaration text
        """
        hat = ".subckt " + self.name + ' ' + ' '.join(self.terminals) + "\n"
        for decl in self.elements:
            hat += decl.synthesize_declaration()
        hat += ".ends " + self.name + '\n\n\n'
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
        synthesized_string += ' '.join(self.terminals) + ') '
        synthesized_string += self.module
        return synthesized_string
    
    def print_description(self) -> str:
        info = "Name: {}\tModule: {}\tTerminals: {}\t".format(self.name, self.module, ', '.join(self.terminals))
        return info



class Mosfet(NestedElement):
    params: dict

    def __init__(self, name: str, module: str, terminals: list[str], params=None) -> None:
        super().__init__(name, module, terminals)
        self.params = params

    def modify_width(self, new_width: float) -> None:
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
        self.params['w'] = new_width

    def modify_length(self, new_length: float) -> None:
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
        self.params['l'] = new_length
    
    def synthesize_declaration(self) -> str:
        """
        Synthesizes MOSFET declaration

        Returns
        -------
            str Syntesized declaration
        """
        synth_string = super().synthesize_declaration()
        for key in self.params:
            synth_string += (key+'='+str(self.params[key])+ ' ')
        synth_string += '\n'
        return 'M'+synth_string
    
    def print_description(self) -> str:
        info = super().print_description() + ' '
        for key in self.params:
            info += (key+': '+str(self.params[key])+ ' ')
        info += '\n'
        return info


class NestedSubCkt(NestedElement):
    """
    Neseted subcircuit representation
    e.g. I0 (a1 a2 a3 gnd) subckt
    """
    params: dict
    def __init__(self, name: str, module: str, terminals: list[str], params: dict=None) -> None:
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
        ----------
            params: dict[str,int]
        
        Returns
        -------
            None
        """
        super().__init__(name=name, module=module, terminals=terminals)
        self.params = params
    
    def print_description(self) -> str:
        info = super().print_description()
        if self.params != None:
            for key in self.params:
                info += (key+': '+str(self.params[key])+ ' ')
            info += '\n'
        return info
    
    def synthesize_declaration(self) -> str:
        """
        Synthesizes instance declaration

        Returns
        -------
            str Syntesized declaration
        """
        synth_string = super().synthesize_declaration() + ' '
        if self.params != None:
            for key in self.params:
                synth_string += (key+'='+str(self.params[key])+ ' ')
        synth_string += '\n'
        return 'I' + synth_string
