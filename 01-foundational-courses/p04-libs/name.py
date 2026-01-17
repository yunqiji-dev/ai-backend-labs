# Example 1
import sys

print("Hello, My name is", sys.argv[1])


# Example 2
import sys

try:
    print("Hello, My name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


# Example 3
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, My name is", sys.argv[1])


# Example 4
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, My name is", sys.argv[1])


# Example 5
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, My name is", arg) 