import wikipedia
import sys

lang = "ES"
searchFor = ""

if len(sys.argv)>1:
    searchFor = sys.argv[1]
if len(sys.argv)>2:
    lang = sys.argv[2]

wikipedia.set_lang(lang)
obj = ""
if searchFor != "":
    obj = wikipedia.summary(searchFor,sentences=3)
 
#obj = wikipedia.search("Valencia")

print (obj)
