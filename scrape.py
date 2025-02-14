#!/home/tomh/craigslist/venv/bin/python3

import os,sys
from requests import get
from bs4 import BeautifulSoup as bs
import json


response = get('https://milwaukee.craigslist.org/search/cta?auto_make_model=honda&auto_title_status=1&bundleDuplicates=1&max_auto_miles=1000000&max_price=41000&min_price=1000&postedToday=1#search=1~list~0~0')

#`print(response.text)

html_soup = bs(response.text,'html.parser')

sr_json = html_soup.find('script', { 'id':'ld_searchpage_results'})

srobj = json.loads(sr_json.get_text())

print(srobj)

item = srobj['itemListElement'][0]['item']

title=item['name']
offers=item['offers']
price=offers['price']
currency=offers['priceCurrency']
state=offers['availableAtOrFrom']['address']['addressRegion']
city=offers['availableAtOrFrom']['address']['addressLocality']

cmdline = (f"""curl --url smtp://mobile.charter.net:25/ --mail-from 'tomviolin@spectrum.net' \
        --mail-rcpt 'tomviolin@spectrum.net' \
        -F "={currency}{price}:{title} ;type=text/plain" \
        -H "Subject: {currency}{price}:{title}" """)


print("\n\n"+cmdline)

