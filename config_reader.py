from arch_reader import Architecture
import configparser
from configparser import ConfigParser, SectionProxy
import json


class Config:
    # Generation params
    # Horizontal size
    word_size = 0
    # Vertical size
    num_words = 0
    # Output file name
    output_name = ""
    # Architecture name
    arch = ""
    # Physics params
    # Physical simulation file
    phys_sim = ""
    # Check LVC
    lvc = False
    # Check DRC
    drc = False
    # Misc params
    # Make pdf
    pdf_output = False

    #aux_filename
    filename: str

    def __open_config(self, filename: str):
        config = configparser.ConfigParser()
        config.read(filename)
        self.filename = filename
        return config

    def __parse_config(self, config: ConfigParser):
        generation_section = config['GENERATION']
        physics_section = config['PHYSICS']
        misc_section = config['MISC']
        self.__parse_generation(generation_section)
        self.__parse_physics(physics_section)
        self.__parse_misc(misc_section)

    def __parse_generation(self, config: SectionProxy):
        self.word_size = int(config['word_size'])
        self.num_words = int(config['num_words'])
        self.output_name = config['output_name']
        self.arch = config['arch']

    def __parse_physics(self, config: SectionProxy):
        self.phys_sim = config['phys_sim']
        self.lvc = config.getboolean('lvc')
        self.drc = config.getboolean('drc')

    def __parse_misc(self, config: SectionProxy):
        self.pdf_output = config.getboolean('pdf_output')

    def __parse_array(self, value: str):
        return json.loads(value)

    def load_arch(self):
        return Architecture(self.arch, self.word_size, self.num_words)

    def __init__(self, filename: str):
        config = self.__open_config(filename)
        self.__parse_config(config)
    
    def print_data(self) -> None:
        report_template = "Config:\n\tName: {0}\n\tWord size: {1}\n\tAmount of words: {2}\n\tOutput file: {3}\n\tArch name: {4}\n\tPhysical sinulation file: {5}\n\tCheck LVC: {6}\n\tCheck DRC: {7}\n\tPDF Output: {8}\n\n"
        return report_template.format(self.filename, self.word_size, self.num_words, self.output_name, self.arch, self.phys_sim, self.lvc, self.drc, self.pdf_output)
