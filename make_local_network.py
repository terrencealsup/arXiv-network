import urllib2
from bs4 import BeautifulSoup as bs
from collections import Counter

"""
Returns a list of the names of co-authors to the input author.
"""
def get_coauthors(author):
    i = author.index(' ')
    url = 'http://export.arxiv.org/api/query?search_query=au:'+author[:i]+'%20'+author[i+1:]+'&start=0&max_results=100'

    data = urllib2.urlopen(url)
    soup = bs(data, "lxml")

    coauthors = []

    for e in soup.find_all("entry"):
        authors_t = e.find_all("author")
        authors = []
        for x in authors_t:
            authors.append(x.contents[1].string)
        if author in authors:
            coauthors += authors
    return Counter(coauthors)




search = raw_input("Who do you want to search for?\n")

print("\n")



print get_coauthors(search)




