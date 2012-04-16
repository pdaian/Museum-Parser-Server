from BeautifulSoup import BeautifulSoup as bs
import urllib2,re

# Exhibit Class, One Instance per Exhibit
class Exhibit:
    def __init__(self, title, startdate, enddate, url, image):
        self.title = title
        self.startdate = startdate        
        self.enddate = enddate
        self.url = url
        self.image = image

# Museum dictionary, str:list(Exhibit)
museums = {}

# Fetch and parse MOMA with BeautifulSoup
url = "http://www.moma.org/explore/exhibitions/on_view"
content = urllib2.urlopen(url).read()
soup = bs(content)
exhibits = soup.findAll('ol')
assert str(exhibits[0]["class"]) == "exhibitions"
for exhibit in exhibits[0].contents:
    try:
	print str(exhibit.h3.contents)
    except:
	# Indicates a malformed entry, possible a newline
	pass
