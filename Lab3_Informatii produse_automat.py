import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime


# Implement a function for obtaining all the products for jewelry category
def jewelry_products(jewelry_category):
    page = urllib2.urlopen(jewelry_category)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    links = soup.select('div.s-item__info > a')

    products_links = []
    for link in links:
        url = link.get('href')
        products_links.append(url)

    return products_links


# Implement extraction of details for a product
def parse(product_page):
    page = urllib2.urlopen(product_page)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    try:
        # Take out the <div> of name and get its value
        name_box = soup.find('h1', attrs={'class': 'it-ttl'})
        name = name_box.text.strip()  # strip() is used to remove starting and trailing

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

        return name, price, condition, quantity
    except AttributeError:
        print("NoneType")


# Implement extraction of details for all products from Jewelry category
quote_pages = jewelry_products("https://www.ebay.com/b/Fashion-Jewelry/10968/bn_2408529")
print(quote_pages)


products = []
for quote_page in quote_pages:
    try:
        product = parse(quote_page)
        product.append(products)
    except AttributeError:
        print("Invalid Url: ", quote_page)

with open('all_products.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)

    for name, price, condition, quantity in products:
        writer.writerow([name, price, condition, quantity, datetime.now()])
