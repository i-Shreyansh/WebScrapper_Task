from bs4 import BeautifulSoup
import requests


class Scrapping:
    def __init__(self) -> None:
        pass
        
        
    def scrape_projects(self,url):
        # Fetch the HTML content
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch {url}")
            return None

        # Parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all text from the section
        all_text = soup.body.get_text()

        return all_text
