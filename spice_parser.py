import re

import spice_elements


class SubCktParser:

    #list of subcircuits
    subs: list[spice_elements.SubCktDecl]

    def open_sp_file(self, path: str) -> str:
        with open(path) as sp:
            return sp.read()

    def parse_subckt_decls(self, sp_text: str) -> list[str]:
        subckt_re = re.compile(
            r"((subckt)|(SUBCKT))\s+([\w]+)\s+((\w+(\s+)?)+)$", re.M)
        res = subckt_re.findall(sp_text)
        hats = [(i[3], i[4]) for i in res]
        return hats

    def get_subckts_content(self, sp_text: str, hats: list) -> list[str]:
        comp_head = [r"((subckt)|(SUBCKT))\s+" + h[0] + r"\s+" +
                     h[1] + r"$(.+)ends\s+"+h[0] for h in hats]
        rex = [re.compile(i, re.M | re.S) for i in comp_head]
        conts = [r.findall(sp_text) for r in rex]
        c = [c[0][3][1::] for c in conts]
        return c

    def parse_terminals(self, hats: list) -> list[list[str]]:
        new_hats = [[h[0], h[1].split()] for h in hats]
        return new_hats

    def parse_content(self, lines: str) -> list:
        split_lines = [l.splitlines() for l in lines]
        return split_lines

    def parse_subs(self, f: str) -> list:
        hats = self.parse_subckt_decls(f)
        content = self.get_subckts_content(f, hats)
        hats = self.parse_terminals(hats)
        pc = self.parse_content(content)
        subs = []
        for s in range(len(hats)):
            subs.append(self.make_single_sub(hats[s], pc[s]))
        return subs

    def make_single_sub(self, hat, lines) -> spice_elements.SubCktDecl:
        pl = []
        for i in range(len(lines)):
            pl.append(ElementParser(lines[i]).get_element())
        sub = spice_elements.SubCktDecl(hat[0], hat[1], pl)
        return sub

    def __init__(self, filename: str) -> None:
        f = self.open_sp_file(filename)
        self.subs = self.parse_subs(f)

    def get_subs(self) -> list:
        return self.subs


class ElementParser:
    element: None

    def parse_element(self, description: str):
        type_estimator = re.compile(r"^\s*((\w)[\d\w]+)")
        ident = type_estimator.findall(description)[0][1]
        if ident == 'M':
            return self.parse_mosfet(description)
        if ident == 'X':
            return self.parse_nested(description)

    def parse_nested(self, descr: str):
        name = self.parse_ident(descr)
        terminals = self.parse_terminals(descr)
        module = self.parse_module(descr)
        return spice_elements.NestedSubCkt(name, module=module, terminals=terminals)

    def parse_mosfet(self, descr: str):
        name = self.parse_ident(descr)
        terminals = self.parse_terminals(descr)
        module = self.parse_module(descr)
        params = self.parse_params(descr)
        return spice_elements.Mosfet(name, module, terminals, params['w'], params['l'])

    def parse_ident(self, descr: str):
        name = re.findall(r"^\s*(\w([\d\w]+))", descr)[0][0][1]
        return name

    def parse_terminals(self, descr: str):
        terminals = re.findall(r"\((.+)\)", descr)[0].split()
        return terminals

    def parse_module(self, descr: str):
        module = re.findall(r"\)\s+(\w+)", descr)[0]
        return module

    def parse_params(self, descr: str):
        params = re.findall(r"(\w+)\=([\w\.]+)", descr)
        dic = dict()
        for i in params:
            dic[i[0]] = float(i[1])
        return dic

    def __init__(self, descr: str) -> None:
        self.element = self.parse_element(descr)

    def get_element(self):
        return self.element


# Test
# parser = SubCktParser("decoder_test.sp").get_subs()
# print(parser)
