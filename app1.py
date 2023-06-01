import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Perform scraping operations here
    # Example: Get the title of the webpage
    title = soup.title.string

    return title

def main():
    st.title("Web Scraper")

    # Get the URL input from the user
    url = st.text_input("Enter the website URL:")

    if st.button("Scrape"):
        # Call the scrape_website function
        result = scrape_website(url)

        # Display the scraped data
        st.write("Title:", result)

if __name__ == "__main__":
    main()
