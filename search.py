import urllib2
import HTMLParser
import re

import parse

urlPrefix="http://worldwide.espacenet.com"

def searchResult(wId):
    opener = urllib2.build_opener()
    url=urlPrefix+"/searchResults?compact=false&ST=singleline&locale=en_EP&DB=EPODOC&query="+wId
    f = opener.open(url)
    html = f.read()

    html_parser = HTMLParser.HTMLParser()
    return html_parser.unescape(html)
    
def parseURL(html):
    URL='' 
    pattern = re.compile(r'(.*)(class="publicationLinkClass".*?href=")(.+?)(">)',re.S)
    match = pattern.match(html)
    if match:
        URL=match.group(3)
    return URL

def crawlResult(url):
    opener = urllib2.build_opener()
    url=urlPrefix+url
    f = opener.open(url)
    html = f.read()
    html_parser = HTMLParser.HTMLParser()
    return html_parser.unescape(html).replace('\n','')

def getResult(wId):
    result=searchResult(wId);
    url=parseURL(result)
    return crawlResult(url);

    