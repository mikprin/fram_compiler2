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

if __name__ == '__main__':
    start_time = time.perf_counter()
    parser = argparse.ArgumentParser(description="Pass memory config")
    parser.add_argument('configuration', metavar='C', type=str, help="configuration file name")
    parser.add_argument('-v', '--verbose', help = 'Set debug level and execute (0 for almost no debug , 5 for full debug)', type=int, default=0)

    args = parser.parse_args()
    compiler = FramCompiler(args.configuration)
    compiler.print_compiler_data()
    end_time = time.perf_counter()
    compilation_time = end_time - start_time
    print("Compilation finished in " + str(compilation_time))
