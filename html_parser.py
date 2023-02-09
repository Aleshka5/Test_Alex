from bs4 import BeautifulSoup
from os import listdir

def take_photo_urls():
    """
    Этот парсер работает с HTML документами.
    Его задача - найти нужные изображения в HTML разметке.

    :return [first_urls_array, second_urls_array]: Возвращает два массива со ссылками
    на изображения. В первом - ссылки на изображения одежды с людьми, во втором - без людей.

    """
    # Получаем все полученные с предыдущего пункта HTML документы
    only_htmls = [file for file in listdir('templates') if bool('.html' in file)]

    # Проверяем наличие лишних файлов в директории
    if len(only_htmls) == 0:
        return [[],[]]

    urls_h = []  # Массив (List) для фото с людьми
    urls_cl = [] # Массив для фото без людей

    # Проходим по всем документам
    for file in only_htmls:
        with open('templates/'+file,'r') as html_text:
            soup = BeautifulSoup(html_text, 'html.parser')
            for parent in soup.find_all('picture', tabindex='0'): # Получаем все теги <picture>
                urls_h.append(parent.findChildren("source", media="(min-width: 768px)")[0]['srcset']) # Ссылки на нужные фото с людьми
                urls_cl.append(parent.findChildren("img", tabindex='0')[0]['src']) # Ссылки на нужные фото одежды без людей
    print(len(urls_h),len(urls_cl))
    assert  len(urls_h) == len(urls_cl) # Проверка что все фото имеют пару (Не защищает от дублирований)
    return [urls_h,urls_cl]

if __name__ == '__main__':
    take_photo_urls()



