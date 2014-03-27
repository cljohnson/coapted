import os
import os.path
path = os.path.expanduser('~/nltk_data')
if not os.path.exists(path):
    os.mkdir(path)
os.path.exists(path)

import nltk.data
from nltk.corpus.reader import WordListCorpusReader
from nltk.tokenize import line_tokenize
from BeautifulSoup import BeautifulSoup
import re
nltk.data.load('banbagsfb.txt', format='raw')
reps = {'&#8220;':'"', '&#8221;':'"', '&#8217;':"'", '&#8250;':'', 'end of .post-entry':'', chr(10):'', '\r\n':'', '&#92;&#114;&#92;&#110;':''}
def main():
    reader = WordListCorpusReader(path, ['banbagsfb.txt'])
    pages = line_tokenize(reader.raw())
    thispage = pages[4]
    thispage = thispage.raw()

    """
    The easiest way to deal with strings in Python that contain escape characters and quotes is to triple double-quote the string (""") and prefix it with r. For example:
    my_str = r"""This string would "really "suck"" to write if I didn't
    know how to tell Python to parse it as "raw" text with the 'r' character and
    triple " quotes. Especially since I want \n to show up as a backlash followed
    by n. I don't want \0 to be the null byte either!"""

    The r means "take escape characters as literal". The triple double-quotes (""") prevent single-quotes, double-quotes, and double double-quotes from prematurely ending the string.

    """

    m = re.search("(\d)", thispage)
    thisitem = m.group(0)
    m = re.search("(\d\d\D\d\d)", thispage)
    thisdate = m.group(0)
    starturl = thispage.find('http')
    endurl = thispage.find(' ', starturl)-2
    thisurl = thispage[starturl:endurl] 
    soup = BeautifulSoup(thispage)
    newpage = soup.findAll(text=True)
    html = replace_all(newpage, reps)
    html = html[11:len(html)]
    postdate = html[0:5]
    posttext = html[5:len(html)]
    print "post date = " + postdate
    print "post text = " + posttext

def replace_all(txt, reps):
    for i, j in reps.iteritems():
        txt = txt.replace(i, j)
    return text

if __name__ == "__main__":
    main()