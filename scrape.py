from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    url = request.args.get('url')
    if url:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the <h1>, <h2>, and <p> tags on the page
        h1_tags = soup.find_all("h1")
        h2_tags = soup.find_all("h2")
        p_tags = soup.find_all("p")

        # Prepare the scraped data as HTML string
        scraped_data = ""
        for tag in h1_tags:
            scraped_data += f"<h1>{tag.text}</h1>"
        for tag in h2_tags:
            scraped_data += f"<h2>{tag.text}</h2>"
        for tag in p_tags:
            scraped_data += f"<p>{tag.text}</p>"

        return scraped_data

    return "No URL specified."

if __name__ == '__main__':
    app.run()
