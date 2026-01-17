# Example 1
import sys

import cowsay

if len(sys.argv) == 2:
    cowsay.cow("hello," + sys.argv[1])

# Example 2
import sys

import cowsay

if len(sys.argv) == 2:
    cowsay.trex("hello," + sys.argv[1])
