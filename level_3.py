from next_level import next_level
from urllib import request
from collections import Counter
import re

page = request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")

#Get list of each lines
code = page.readlines()[22:1271]
strcode = b"".join(code)

#Find least used characters
letters = re.findall(b"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", strcode)
f = b"".join(letters)

#Figured out it was linkedlist.php
