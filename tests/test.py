import os
import sys

import yaml

# Read yamole from the current source
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.normpath(os.path.dirname(TEST_DIR)))


from yamole import YamoleParser

with open(os.path.join(TEST_DIR, 'source.yaml')) as file:
    parser = YamoleParser(file)
    actual = parser.data

with open(os.path.join(TEST_DIR, 'expected.yaml')) as file:
    expected = yaml.safe_load(file)

assert(actual == expected)

# We can't test the .dumps() method as there's no guarantee the keys in the
# output will always be sorted the same way.
