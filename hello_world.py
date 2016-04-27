Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
import json
title = raw_input("Enter word to search: ")
print "Word: ",title
url = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase='+title.lower()+'&pretty=true'
result = json.load(urllib.urlopen(url))
length = len(result["tuc"][0]["meanings"])
print "Meaning: ", result["tuc"][0]["meanings"][0]["text"]
print "--Other: "
for i in range(1,length):
         print "-- :",result["tuc"][0]["meanings"][i]["text"]
