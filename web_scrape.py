import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

# URL of the site to scrape
url = "http://books.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Open a CSV file for writing
with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Title', 'Price', 'Link'])

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all book containers
        books = soup.find_all('article', class_='product_pod')

        # Extract the title, price, and link of each book
        for book in books:
            # Get the title of the book
            title = book.h3.a['title']
            
            # Get the price of the book
            price = book.find('p', class_='price_color').text
            
            # Get the relative link to the book's detail page
            relative_link = book.h3.a['href']
            
            # Convert the relative link to an absolute URL
            book_link = urljoin(url, relative_link)
            
            # Write the data to the CSV file
            writer.writerow([title, price, book_link])
        
        print("Data successfully written to books.csv.")
    else:
        print("Failed to retrieve the webpage.")

