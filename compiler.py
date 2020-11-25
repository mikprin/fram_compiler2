import argparse
import time
from config_reader import Config

if __name__ ==  '__main__':
    #Code execution in case of direct call


    start_time = time.perf_counter()
    # Init parser
    parser = argparse.ArgumentParser(description="Pass memory config")
    parser.add_argument('configuration', metavar='C', type=str, help="configuration file name")
    parser.add_argument('-v' , '--verbose' , help = "Set debug level and execute (0 for almost no debug , 5 for full debug)", type = int , default = self.Config.debug_level )

    args = parser.parse_args()

    config = Config(args.configuration)

	if args.verbose != self.Config.debug_level:
		config = args.verbose




    end_time = time.perf_counter()
    compilation_time = end_time - start_time


class Fram_Compiler:
    """docstring for Fram_Compiler."""
    def __init__(config, *args , **kwargs):
        self.config = config
        self.args = args

        arch = config.load_arch()
