from next_level import next_level
from urllib import request
from collections import Counter

page = request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

#Get list of each lines
code = page.readlines()[38:1258]
strcode = b"".join(code)

#Find least used characters
Counter(strcode.decode("utf-8"))

#Figured out it was equality
next_level("equality")