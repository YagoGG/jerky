import os
import sys

import yaml

# Read yamole from the current source
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.normpath(os.path.dirname(TEST_DIR)))


from yamole import YamoleParser

parser = YamoleParser(os.path.join(TEST_DIR, 'source.yaml'))
actual = parser.data

with open(os.path.join(TEST_DIR, 'expected.yaml')) as file:
    expected = yaml.load(file)

assert(actual == expected)
