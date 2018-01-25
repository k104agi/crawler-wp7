from bs4 import BeautifulSoup

source = open('melon.html', 'rt').read()
soup = BeautifulSoup(source, 'lxml')

for tr in soup.find_all('tr', class_='lst50'):
    title = tr.find('div', class_='rank01').find('a').text

    singer = tr.find('div', class_='rank02').find('a').text

    album = tr.find('div', class_='rank03').find('a').text

    print([title, singer, album])
    print('  ')

#    td_list = tr.find_all('td')

#for a in soup.find_all('td'):
#    print(td)