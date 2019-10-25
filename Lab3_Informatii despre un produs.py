import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# specify the url
quote_page = 'https://www.ebay.com/itm/Fashion-Women-14K-Solid-Rose-Gold-Stack-Twisted-Ring-Wedding-Party-Women-Jewelry/123124656321?hash=item1caacd28c1:m:mFQFxGYmDXl8QV1UQoMjmOA&var=423812277032'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# get the index name of the jewelry
name_box = soup.find('h1', attrs={'class': 'it-ttl'})
name: object = name_box.text
print(name)

# get the index price of the jewelry
price_box = soup.find('span', attrs={'class': 'notranslate'})
price = price_box.text
print(price)

# get the index condition of the jewelry
condition_box = soup.find('div', attrs={'class': 'u-flL condText'})
condition = condition_box.text
print(condition)

# get the index quantity available of the jewelry
quantity_box = soup.find('a', attrs={'class': 'vi-txt-underline'})
quantity = quantity_box.text
print(quantity)


# open a csv file with append, so old data will not be erased
with open('detalii_produs.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, condition, quantity, datetime.now()])


