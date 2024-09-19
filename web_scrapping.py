from bs4 import BeautifulSoup
import pandas as pd

# Read and parse the HTML file
with open("Amazon.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Lists to store the data
product_names = []
product_prices = []
product_reviews = []

# Find all divs with the class "a-section a-spacing-small a-spacing-top-small"
divs = soup.find_all("div", class_="a-section a-spacing-small a-spacing-top-small")

# Loop through each div and extract the desired information
for div in divs:
    # Try to find the product name
    try:
        product_name = div.find("div", {"data-cy": "title-recipe", "class": "a-section a-spacing-none puis-padding-right-small s-title-instructions-style"}).get_text(strip=True)
    except:
        product_name = " "

    # Try to find the product review
    try:
        product_review = div.find("div", {"data-cy": "reviews-block", "class": "a-section a-spacing-none a-spacing-top-micro"}).get_text(strip=True)
    except:
        product_review = " "

    # Try to find the product price
    try:
        product_price = div.find("span", class_="a-price-whole").get_text(strip=True)
    except:
        product_price = " "

    # Append the extracted data to the lists
    product_names.append(product_name)
    product_prices.append(product_price)
    product_reviews.append(product_review)

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame({
    "Product Name": product_names,
    "Product Price": product_prices,
    "Product Review": product_reviews
})

# Write the DataFrame to an Excel file
df.to_excel("Amazon_Products.xlsx", index=False)

print("Data has been successfully written to 'Amazon_Products.xlsx'.")


