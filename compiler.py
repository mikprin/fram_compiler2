from compiled_spice_scheme import CompiledSpice
from arch_unit import Core
import argparse
import time

from arch_reader import Architecture
from config_reader import Config

# parser = argparse.ArgumentParser(description="Pass memory config")
# parser.add_argument('configuration', metavar='C', type=str, help="configuration file name")

# args = parser.parse_args()
# config = Config(args.configuration)
# arch = config.load_arch()
# print(arch)

class FramCompiler:
    """Initialize new FramCompiler object"""
    config: Config
    arch: Architecture

    def __init__(self, config) -> None:
        self.config = config
        self.args = args
        self.config = Config(self.config)
        self.arch = self.config.load_arch()
    
    def print_compiler_data(self) -> None:
        print("FRAM Compiler:")
        config = self.config.print_data()
        config += self.arch.print_data()
        print(config)

    def compile_spice(self) -> str:
        #Evaluating connections
        core_lines = self.arch.evaluate_core_lines(self.config.word_size, self.config.num_words)
        left_lines = self.arch.evaluate_side_lines(self.arch.left, self.config.num_words, Core.LineType.VERTICAL)
        right_lines = self.arch.evaluate_side_lines(self.arch.right, self.config.num_words, Core.LineType.VERTICAL)
        top_lines = self.arch.evaluate_side_lines(self.arch.top, self.config.word_size, Core.LineType.HORIZONTAL)
        bottom_lines = self.arch.evaluate_side_lines(self.arch.bottom, self.config.word_size, Core.LineType.HORIZONTAL)
        #Create new compiled scheme
        cs = CompiledSpice()
        #Adding subckts with connections
        h = self.config.word_size
        v = self.config.num_words
        for i in range(v):
            for j in range(h):
                cs.add_subckt(self.arch.central.pkg, core_lines[i][j])
        for l in range(len(self.arch.left)):
            for i in range(v):
                cs.add_subckt(self.arch.left[l].pkg, left_lines[l][i])
        for l in range(len(self.arch.right)):
            for i in range(v):
                cs.add_subckt(self.arch.right[l].pkg, right_lines[l][i])
        for l in range(len(self.arch.top)):
            for i in range(h):
                cs.add_subckt(self.arch.top[l].pkg, top_lines[l][i])
        for l in range(len(self.arch.bottom)):
            for i in range(h):
                cs.add_subckt(self.arch.bottom[l].pkg, bottom_lines[l][i])
        return cs.build()

    def compile_scheme(self):
        spice = self.compile_spice()
        sp = open(self.config.arch+'.sp', 'w')
        sp.write(spice)
        sp.close()

if __name__ == '__main__':
    start_time = time.perf_counter()
    parser = argparse.ArgumentParser(description="Pass memory config")
    parser.add_argument('configuration', metavar='C', type=str, help="configuration file name")
    parser.add_argument('-v', '--verbose', help = 'Set debug level and execute (0 for almost no debug , 5 for full debug)', type=int, default=0)

    args = parser.parse_args()
    compiler = FramCompiler(args.configuration)
    if args.verbose == 1: compiler.print_compiler_data()
    compiler.compile_scheme()
    end_time = time.perf_counter()
    compilation_time = end_time - start_time
    print("Compilation finished in " + str(compilation_time))
