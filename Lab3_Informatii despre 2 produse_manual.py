import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# specify the url
quote_page = ['https://www.ebay.com/itm/Fashion-Women-14K-Solid-Rose-Gold-Stack-Twisted-Ring-Wedding-Party-Women-Jewelry/123124656321?hash=item1caacd28c1:m:mFQFxGYmDXl8QV1UQoMjmOA&var=423812277032',
              'https://www.ebay.com/itm/14k-gold-7-tiny-diamond-pieces-of-exquisite-small-fresh-ladies-engagement-ring/153461411715?hash=item23bb034f83:m:mdlHi1A-rWfFvhYESBTvG0g&var=453414768000']

# # query the website and return the html to the variable ‘page’
# page = urllib2.urlopen(quote_page)
#
# # parse the html using beautiful soup and store in variable `soup`
# soup = BeautifulSoup(page, 'html.parser')

# for loop
data = []
for pg in quote_page:
    # query the website and return the html to the variable ‘page’
    page = urllib2.urlopen(pg)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'it-ttl'})
    name = name_box.text.strip() # strip() is used to remove starting and trailing

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

    # save the data in tuple
    data.append((name, price, condition, quantity))

# open a csv file with append, so old data will not be erased
with open('detalii_produse_manual.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    # The for loop
    for name, price, condition, quantity in data:
        writer.writerow([name, price, condition, quantity, datetime.now()])
