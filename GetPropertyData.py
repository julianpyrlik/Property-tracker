import time

from bs4 import BeautifulSoup
import requests


class GetPropertyData:
    def __init__(self):
        response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
        webpage = response.text
        self.soup = BeautifulSoup(webpage, 'html.parser')
        self.get_data()

    def get_data(self):
        time.sleep(1)
        # get links for all listings
        links = self.soup.select('.ListItem-c11n-8-84-3-StyledListCardWrapper a')
        self.link_list = [link.get('href') for link in links]
        print(self.link_list)

        # get prices for all the listings
        prices = self.soup.select('span[data-test="property-card-price"]')
        self.prices_list = [price.text.split('+')[0].split('/')[0] for price in prices]
        print(self.prices_list)

        # get the adresses
        addresses = self.soup.find_all(name='address')
        self.address_list = [address.text.replace('|', '').replace('  ', ' ').strip() for address in addresses]
        print(self.address_list)
