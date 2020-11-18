import argparse
from config_reader import Config

parser = argparse.ArgumentParser(description="Pass memory config")
parser.add_argument('configuration', metavar='C', type=str, help="configuration file name")

args = parser.parse_args()
config = Config(args.configuration)
arch = config.load_arch()