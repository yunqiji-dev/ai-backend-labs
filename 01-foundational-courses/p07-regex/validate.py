# Example 1
email = input("What's your email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invaild")


# Example 2
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invaild")


# Example 3
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invaild")


# Example 4
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invaild") 


# Example 5
import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invaild")


# Example 6
import re

email = input("What's your email? ").strip()

if re.search("..*@..*", email):
    print("Valid")
else:
    print("Invaild")


# Example 7
import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invaild")
