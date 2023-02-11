from bs4 import BeautifulSoup
from os import listdir

def take_photo_urls():
    """
    This parser works with HTML document.
    It task is - search for the needed images in a HTML document.
    :return [first_urls_array, second_urls_array]: Returns two lists with links to images inside.
    first_urls_array - links to images of the people wearing a particular cloth,
    second_urls_array - links to images of the cloths.

    """
    # Find all the parsed HTML documents
    only_htmls = [file for file in listdir('templates') if bool('.html' in file)]

    # Clear the array of empty items
    if len(only_htmls) == 0:
        return [[],[]]

    urls_h = []  # images of the people wearing a particular cloth
    urls_cl = [] # images of the cloths

    # Find the urls of the images
    for file in only_htmls:
        with open('templates/'+file,'r') as html_text:
            soup = BeautifulSoup(html_text, 'html.parser')
            for parent in soup.find_all('picture', tabindex='0'): # Take all tags <picture>
                urls_h.append(parent.findChildren("source", media="(min-width: 768px)")[0]['srcset'])
                urls_cl.append(parent.findChildren("img", tabindex='0')[0]['src'])
    print(f'The number of image urls: first_list - {len(urls_h)}, second_list - {len(urls_cl)}')
    assert  len(urls_h) == len(urls_cl) # Make sure that all images have pairs
    return [urls_h,urls_cl]

if __name__ == '__main__':
    take_photo_urls()



