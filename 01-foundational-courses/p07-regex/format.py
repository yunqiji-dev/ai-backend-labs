# Example 1
name = input("What's your name? ").strip()
print(f"hello, {name}")


# Example 2
name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first}{last}"
print(f"hello, {name}")


# Example 3
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first}{last}"
print(f"hello, {name}")


# Example 4
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first}{last}"
print(f"hello, {name}")


# Example 5
import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

