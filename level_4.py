from next_level import next_level
from urllib import request
import re


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

#The image is a link
i = 0
suffix = str(63579)

while i < 410:
	page = request.urlopen(url + suffix)
	text = page.read().decode("utf-8")
	print(text)
	suffix = re.search("\d+", text).group()
	i +=1
	
	
#Answer is peak.html