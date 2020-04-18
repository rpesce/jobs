from bs4 import BeautifulSoup
import requests
import csv
import os

# Getting information from the page
# url = "https://www.facebook.com/careers/jobs/2031957310217898/"
# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())

# for text in soup.find_all('p'):  # [2].get_text()
#    print(text.get_text())


# Specify URL and get HTML
url = 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm'
page = requests.get(url)

# Create BeautifulSoup object and parse HTML
soup = BeautifulSoup(page.text, "html.parser")

# Identify links in the bottom and use decompose() to remove it from parse tree
bottom_links = soup.find(class_='AlphaNav')
bottom_links.decompose()

# Define the path for saving the csv
filepath = os.path.join("/Users/Pesce/desktop/", "z-artists-name.csv")

# Opening the csv and writing name + link
f = csv.writer(open(filepath, 'w'))
f.writerow(['Name', 'Link'])

# Find div where the list pf names is, and find all artists within th e list
artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

# Print all artists names
for artist in artist_name_list_items:
    names = artist.contents[0]
    links = 'https://web.archive.org' + artist.get('href')
    print("Name:", names)
    print("Link:", links)
    print()

    # Add each row to the csv
    f.writerow([names, links])


