import time
import requests
import os


def get_photos(urls_humans,urls_clothes):
    """
    This parser downloads images from the internet to a folder named "imgs"

    :param urls_humans:  - urls for images of the people wearing a particular cloth
    :param urls_clothes: - urls for images of the cloths
    Note: urls_humans[i] correspond urls_clothes[i], consisting of images of
    a person wearing a certain cloth and the cloth itself.
    :return: None. - All data saves to folders:
    - imgs:
        - with_human (folder for images of the people wearing a particular cloth)
        - without_human (folder for images of the cloths)

    """

    # Create a folders, if not exists
    if not os.path.exists('imgs/with_human'):
        os.makedirs("imgs/with_human")
    if not os.path.exists('imgs/without_human'):
        os.makedirs("imgs/without_human")

    i = 1  # Current index of image pairs
    count_photos = len(urls_humans) # The number of links to images
    index_bad_photos = count_photos # Current index of identical image pairs (I think these are bad image pairs)

    # Take each image pairs
    for url_human,url_cloth in zip(urls_humans, urls_clothes):

        # Just debug progressbar
        if i % 5 == 0:
            print(f'The percent of dataset collection: {round(((i + count_photos-index_bad_photos)/count_photos)*100,2)}%')

        # Try to make request
        while True:
            try:
                response1 = requests.get(url=url_human)
                time.sleep(1)
                response2 = requests.get(url=url_cloth)
                time.sleep(1)
                print('Request completed successfully.')
                print(f'First request status: {response1.status_code}')
                print(f'Second request status: {response1.status_code}')
                print('#' * 20)
                break

            except:
                print('Request error.')
                print(f'First request status: {response1.status_code}')
                print(f'Second request status: {response1.status_code}')
                print('#' * 20)
                print('Wait 30 sec')
                time.sleep(30)
                print('Next try')

        # Save images to particular folders
        if response1.content != response2.content:
            with open(f'imgs/with_human/img{i}.jpg', 'wb') as image:
                image.write(response1.content)

            with open(f'imgs/without_human/img{i}.jpg', 'wb') as image:
                image.write(response2.content)
            i += 1

        # If we find an identical image pairs, will save it in the end of image list.
        # (i mean image pairs, for which there is not exist image of the people wearing a particular cloth)
        else:
            print('Images - identical')
            with open(f'imgs/with_human/bad_img{index_bad_photos}.jpg', 'wb') as image:
                image.write(response1.content)

            with open(f'imgs/without_human/bad_img{index_bad_photos}.jpg', 'wb') as image:
                image.write(response2.content)
            index_bad_photos -= 1
        print(f'{i} : {index_bad_photos}')
    print('The percent of dataset collection: 100%')
if __name__ == '__main__':
    get_photos([],[])


