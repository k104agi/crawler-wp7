import re
from bs4 import BeautifulSoup
from utils import get_top100_list

source = open('melon.html', 'rt').read()
soup = BeautifulSoup(source, 'lxml')

if __name__ == '__main__':
    get_top100_list()
