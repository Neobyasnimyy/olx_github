from parser import *
#from test import spisok

BASE_URL = 'https://www.olx.ua/obyavlenie/prodam-uyutnyy-dom-p-g-t-frunzovka-IDlwFxQ.html'
Base_Find_url = 'https://www.olx.ua/nedvizhimost/prodazha-kvartir/odessa/?currency=USDpro'


def main():
    project_name = input('Save as ... ')
    spisok_ = spisok(get_html(Base_Find_url))
    project = []

    for url in spisok_:
        #print(url)
        project.append(parse(get_html(url), url))

    #project.append(parse(get_html(BASE_URL), BASE_URL))
    save(project, project_name + '.csv')
""""""

if __name__ == '__main__':
    main()