import parser_selenium
import html_parser
import parser_requests

def scrape_images(url):
    #parser_selenium.parse_the_cite(url)             # Получает код сайта в нескольких пакетах и сохраняет в текущую директорию
    photo_urls = html_parser.take_photo_urls()     # Получает со страниц все ссылки на нужные фотографии
    parser_requests.get_photos(photo_urls[0],photo_urls[1])          # Сохраняет все фоотографии в папку imgs

if __name__ == '__main__':
    url = 'https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204'
    scrape_images(url)
