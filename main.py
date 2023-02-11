import parser_selenium
import html_parser
import parser_requests

def scrape_images(url):
    parser_selenium.parse_the_cite(url) # Gets the website source and places it in a folder named "templates"
    photo_urls = html_parser.take_photo_urls() # Takes all needed links to images from HTML pages
    parser_requests.get_photos(photo_urls[0],photo_urls[1]) # Saves all images to a folder named "imgs"

if __name__ == '__main__':
    url = 'https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204'
    scrape_images(url)
