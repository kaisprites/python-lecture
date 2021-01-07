from bs4 import BeautifulSoup
import requests


def crawl(site, find=[]):
    print('네이버 긁기')
    target = requests.get(site).text
    print('네이버 연결 성공')

    document = BeautifulSoup(target, 'html.parser')
    find_result = []
    for f in find:
        print('find: ' + f)
        titles = document.select(f)
        print(titles)
        if len(titles) != 0:
            print('first string: ' + titles[0].string)
            find_result.append(titles[0].string)
    print(find_result)
    return find_result
