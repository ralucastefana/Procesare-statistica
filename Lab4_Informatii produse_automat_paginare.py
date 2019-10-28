import urllib.request as urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime


# Implement a function for obtaining all the products for jewelry category from all the pages
def jewelry_products(jewelry_category, index, products_links):
    page = urllib2.urlopen(jewelry_category + str(index))

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    links = soup.select('div.s-item__info > a')

    for link in links:
        url = link.get('href')
        products_links.append(url)

    if index == 1:
        return products_links
    return jewelry_products(jewelry_category, index-1, products_links)


# Implement extraction of details for a product
def parse(product_page):
    page = urllib2.urlopen(product_page)

    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    names = []
    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'it-ttl'})
    if name_box == 'NoneType':
        name = 0
    else:
        name = name_box.text.strip()  # strip() is used to remove starting and trailing
    names.append(name)
    print(names)

    prices = []
    # get the index price of the jewelry
    price_box = soup.find('span', attrs={'class': 'notranslate'})
    if price_box == 'NoneType':
        price = 0
    else:
        price = price_box.text
    prices.append(price)
    print(prices)

    conditions = []
    # get the index condition of the jewelry
    condition_box = soup.find('div', attrs={'class': 'u-flL condText'})
    if condition_box == 'NoneType':
        condition = 0
    else:
        condition = condition_box.text
    conditions.append(condition)
    print(conditions)


    #  # get the index quantity available of the jewelry
    # quantity_box = soup.find('a', attrs={'class': 'vi-txt-underline'})
    # if quantity_box == 'NoneType':
    #     quantity = 0
    # else:
    #     quantity = quantity_box.text
    # print(quantity)

    return name, price, condition


# Implement extraction of details for all products from Jewelry category
quote_pages = jewelry_products("https://www.ebay.com/e/fashion/jewelry-under-10-101419?_pgn=", 25, [])
print(quote_pages)


products = []
for quote_page in quote_pages or []:
    # try:
        product = parse(quote_page)
        products += product
        with open('all_products.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([product[0], products[1], products[2], datetime.now()])
    # except AttributeError:
    #     print("Invalid Url: ", quote_page)


# Lab 4
import pandas as pd

test_df = pd.Dataframe({'name': names, 'price': prices, 'condition': conditions})
print(test_df.info())
test_df
test_df.head(3)

test_df = test_df[['name', 'price', 'condition']]
test_df.head()

test_df['price'].unique()
test_df['price'].head(3)

test_df.describe().loc[['min', 'max'], ['price']]


import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (15, 3))
ax = fig.axes
ax.hist(test_df['price'], bins = 10, range = (0,10))