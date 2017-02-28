
import csv
import urllib.request       # библиотека для работы с сетью
from bs4 import BeautifulSoup


def get_html(url):            # получение страницы html
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html, BASE_URL):
    # Beautiful Soup - это парсер для синтаксического разбора файлов HTML/XML
    soup = BeautifulSoup(html, "html.parser")
    telo = soup.find('div', class_='clr offerbody')

    project = {}

    object_name = telo.find('div', class_='offer-titlebox')
    object_name1 = object_name.find('h1')
    address = object_name.find('a', class_='show-map-link')
    added = object_name.find('em').text.strip().split()
    details_object = telo.find('table', class_='details fixed marginbott20 margintop5 full')

    project.update({
        'object_name': object_name1.text.strip(),
        'address': address.text,
        'url': BASE_URL,
        'Информация о публикации': ' '.join(added[:-3]),
    })


    detalils_riadu = details_object.find_all('tr') # все ряды

    for row  in detalils_riadu:   # пеебираем ряды

        cols = row.find_all('table', class_='item')   # столбец

        for cols1 in cols:
            project.update({
                cols1.find('th').text: cols1.find('td', class_='value').text.strip()
            })

    try:
        price = telo.find('div', class_='price-label').text.strip()
    except AttributeError:
        price = None
    project.update({
        'Цена': price
    })

    return project


def save(project, path):  # принимает проэкт и путь к сохранению
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)     # создаем обьект который будет записывать в таблицу данные
        writer.writerow(('object_name', 'address', 'Информация о публикации', 'Цена', 'Объявление от', 'Тип аренды',
                         'Тип квартиры', 'Количество комнат', 'Общая площадь',
                         'Жилая площадь', 'Площадь кухни', 'Тип', 'Этаж', 'Этажность дома', 'url', 'Топ'))
        # Для каждой строки в CSV файле вызовите writer.writerow, передав итерируемый объект (список или кортеж)
        for project in project:
            writer.writerow((project.get('object_name'),
                             project.get('address'),
                             project.get('Информация о публикации'),
                             project.get('Цена'),
                             project.get('Объявление от'),
                             project.get('Тип аренды'),
                             project.get('Тип квартиры'),
                             project.get('Количество комнат'),
                             project.get('Общая площадь'),
                             project.get('Жилая площадь'),
                             project.get('Площадь кухни'),
                             project.get('Тип'),
                             project.get('Этаж'),
                             project.get('Этажность дома'),
                             project.get('url')
                             ))


def spisok(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table', class_='fixed offers breakword ')
    rows = table.find_all('h3', class_='x-large lheight20 margintop5')
    project = []
    for row in rows:
        row_a = row.find('a')
        href = row_a.get('href')
        #print(href[:(href.rfind('html'))] + 'html')
        project.append(
            href[:(href.rfind('html'))] + 'html'
        )
    return project
