from bs4 import BeautifulSoup
import requests
import csv
import os

# Define the path for saving the csv, opening the csv, and writing name + link
filepath = os.path.join("/Users/Pesce/desktop/", "z-artists-name.csv")
f = csv.writer(open(filepath, 'w'))
f.writerow(['Name', 'Link'])


pages = []
# Specify URL for all different pages and get HTML
for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    # Get the HTML and create a BeautifulSoup object
    page = requests.get(item)
    soup = BeautifulSoup(page.text, "html.parser")
    # Identify links in the bottom and use decompose() to remove it from parse tree
    bottom_links = soup.find(class_='AlphaNav')
    bottom_links.decompose()

    # Find div where the list pf names is, and find all artists within th e list
    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    # Print all artists names
    for artist in artist_name_list_items:
        names = artist.contents[0]
        links = 'https://web.archive.org' + artist.get('href')

        # Add each row to the csv
        f.writerow([names, links])