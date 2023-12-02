# web_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_web_page(url):
    try:
        # Fetch the HTML content of the web page
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract clean text from the parsed HTML
        clean_text = soup.get_text(separator='\n', strip=True)

        return clean_text

    except requests.exceptions.RequestException as e:
        print(f"There is an error: {e}")
        return None

if __name__ == "__main__":
