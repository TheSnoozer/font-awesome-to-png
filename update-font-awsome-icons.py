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
for div in b.findAll("div"):
    if 1 == len(div.findAll("i")):
        fontawsomeChar = div.findAll("i")[0].text
        if(len(div.contents) > 2 and fontawsomeChar != ""):
            for tag in div.findAll('small'):
                tag.replaceWith('')

            elements = filter(lambda x: x != '\n' and x != '(alias)', div.findAll(text=True))
            elements = map(lambda x: x.strip(), elements)
            # print str(elements) + " ----- " + str(len(elements))

            fontawsomeChar = fontawsomeChar.replace("&#xf", "")
            name = str(elements[1]).replace("fa-", "")

            print '"'+name+'": ' + 'u("\uf' + fontawsomeChar.replace(";", "") + '"),'
