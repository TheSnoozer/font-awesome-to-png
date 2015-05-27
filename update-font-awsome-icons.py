import sys
import urllib
import BeautifulSoup

# Support Unicode literals with both Python 2 and 3
if sys.version < '3':
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

c = urllib.urlopen("https://fortawesome.github.io/Font-Awesome/cheatsheet/").read()
b = BeautifulSoup.BeautifulSoup(c)
d = {}
for i in b.findAll("div"):
    if 1 == len(i.findAll("i")):
        fontawsomeChar = i.findAll("i")[0].text
        if(len(i.contents) > 2 and fontawsomeChar != ""):
            fontawsomeChar = fontawsomeChar.replace("&#xf", "")
            name = str(i.contents[2].strip()).replace("fa-", "")
            print '"'+name+'": ' + 'u("\uf' + fontawsomeChar + '"),'
