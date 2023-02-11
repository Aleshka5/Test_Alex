import time
import requests
import os


def get_photos(urls_humans,urls_clothes):
    """
    Этот парсер собирает изображения из интернета в папку imgs.

    :param urls_humans:  - urls для изображений одежды на людях
    :param urls_clothes: - urls для изображений одежды без людей
    Note: urls_humans[i] соответствует urls_clothes[i] по типу изображенной одежды
    :return: None. - Не имеет выводимых пераметров. Сохраняет результаты по папкам:
    - imgs:
        - with_human (Папка для фото одежды с людьми)
        - without_human (Папка для фото оджды без людей)

    """
    # Создание структуры папок, если необходимо
    if not os.path.exists('imgs/with_human'):
        os.makedirs("imgs/with_human")
    if not os.path.exists('imgs/without_human'):
        os.makedirs("imgs/without_human")

    i = 1 # Индекс пары различных фото
    count_photos = len(urls_humans) # Количество ссылок на фото
    index_bad_photos = count_photos # Индекс пары одинаковых фото

    # Прохождение по соответствующим изображениям
    for url_human,url_cloth in zip(urls_humans, urls_clothes):

        # Прогресс бар
        if i % 5 == 0:
            print(f'Процесс сбора датасета: {round(((i + count_photos-index_bad_photos)/count_photos)*100,2)}%')

        # Попытка сделать запрос фотографии
        while True:
            try:
                response1 = requests.get(url=url_human)
                time.sleep(1)
                response2 = requests.get(url=url_cloth)
                time.sleep(1)
                print('Запрос обработан успешно.')
                print(f'Статус первого запроса: {response1.status_code}')
                print(f'Статус второго запроса: {response1.status_code}')
                print('#' * 20)
                break

            except:
                print('Ошибка запроса.')
                print(f'Статус первого запроса: {response1.status_code}')
                print(f'Статус второго запроса: {response1.status_code}')
                print('#' * 20)
                print('Ожидание 30 сек')
                time.sleep(30)
                print('Следующая попытка')

        # Сохранение изображений по разным папкам
        if response1.content != response2.content:
            with open(f'imgs/with_human/img{i}.jpg', 'wb') as image:
                image.write(response1.content)

            with open(f'imgs/without_human/img{i}.jpg', 'wb') as image:
                image.write(response2.content)
            i += 1
        # Если два изображения оказались одинаковыми (т.е. для них не
        # существует фото с человеком) сохраняем их в конец списка с особыми названиями
        else:
            print('Фото - одинаковые')
            with open(f'imgs/with_human/bad_img{index_bad_photos}.jpg', 'wb') as image:
                image.write(response1.content)

            with open(f'imgs/without_human/bad_img{index_bad_photos}.jpg', 'wb') as image:
                image.write(response2.content)
            index_bad_photos -= 1
        print(f'i = {i}, b_i = {index_bad_photos}')
    print('Процесс сбора датасета: 100%')
if __name__ == '__main__':
    get_photos([],[])


