from pythoncode.pack01.scrapper import crawl


if __name__ == '__main__':
    crawl('https://www.naver.com', 'a.nav')
    crawl('https://finance.naver.com/', 'span.tx')

    target = ['008700', '005300', '000080', '264900', '041140']
    title = {}
    price = {}
    for x in target:
        title[x] = crawl(f'https://finance.naver.com/item/main.nhn?code={x}', 'h2 *')
        price[x] = crawl(f'https://finance.naver.com/item/main.nhn?code={x}', 'p.no_today *')

    print(title)
    print(price)

    f = open("삼성전자.txt", 'w')
    for x in target:
        f.write(f'{title[x]}: {price[x]}원\n')
    f.close()