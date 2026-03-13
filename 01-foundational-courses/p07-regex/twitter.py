# Example 1
url = input("URL: ").strip()
print(url) 


# Example 2
url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username:{username}")


# Example 3
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username:{username}")


# Example 4
import re

url = input("URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"Username:{username}")


# Example 5
import re

url = input("URL: ").strip()

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"Username:{username}")


# Example 6
import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username:{username}")


# Example 7
import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(2))


# Example 8
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print("Username:", matches.group(2))


# Example 9
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print("Username:", matches.group(1))


# Example 10
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
    if matches.group(1) == "com":
        print("Username:", matches.group(1))


# Example 11
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print("Username:", matches.group(1))
