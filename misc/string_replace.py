import re

s = "a skdfjs\t        \t       ddf  "
ns = s.replace(' ', '').replace("\t", '')
print(ns)

re_ns = re.sub("\s", '', s)
print(re_ns)

# transcript_regex.py
REGEX_REPLACEMENTS = [
    (r"blast\w*", "😤"),
    (r" [-T:+\d]{25}", ""),
    (r"\[support\w*\]", "Agent "),
    (r"\[johndoe\]", "Client"),
]

transcript = """
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!
"""

for old, new in REGEX_REPLACEMENTS:
    transcript = re.sub(old, new, transcript, flags=re.IGNORECASE)

print(transcript)