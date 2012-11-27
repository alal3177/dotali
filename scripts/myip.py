#!/usr/bin/env python

import urllib2
import re

WEBSITE = "http://whatismyipaddress.com/ip-lookup" 

def get_ip_from_url(url):
    try:
        response = urllib2.urlopen(url)
        key = response.read()
        return key.strip(), 
    except urllib2.URLError as exception :
        return False, exception

# http://stackoverflow.com/questions/2890896/extract-ip-address-from-an-html-string-python
def extract_ip_from_html(html_page):
    return re.findall( r'[0-9]+(?:\.[0-9]+){3}', html_page)

def main(website):
    page = get_ip_from_url(website)[0]
    return extract_ip_from_html(page)

if __name__=="__main__":
    print main(WEBSITE)

