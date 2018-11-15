import urllib2
from bs4 import BeautifulSoup as bs
import lxml

url = 'http://export.arxiv.org/api/query?search_query=all:optimal%bellman%20stochastic&start=0&max_results=10'
data = urllib2.urlopen(url)
soup = bs(data, "lxml")
i=1



for e in soup.find_all('entry'):
    print str(i)+": "+e.title.contents[0]
    print "Author(s) : "
    for a in e.find_all("author"):
        print a.contents[1].string

    print "\n"
    i=i+1

