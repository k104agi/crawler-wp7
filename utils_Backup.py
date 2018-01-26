import re
import os
import requests
from bs4 import BeautifulSoup


def get_top100_list(refresh_html=False):
    """
    실시간 차트 1~100위의 리스트 반환
    파일위치:
        현재 파일(모듈)의 위치를 사용한 상위 디렉토리 경로 (crawler디렉토리):
            os.path.dirname(os.path.abspath(__name__))
        1~50위:   data/chart_realtime_50.html
        51~100위: data/chart_realtime_100.html
    """
    # 프로젝트 컨테이너 폴더 경로
    path_module = os.path.abspath(__name__)
    #print(f'path_module: \n{path_module}')

    root_dir = os.path.dirname(path_module)
    #print(f'root_dir: \n{root_dir}')

    # data/ 폴더 경로
    path_data_dir = os.path.join(root_dir, 'data')
    #print(f'path_data_dir: \n{path_data_dir}')

    #print(f'file_path: \n{file_path}')

    os.makedirs(path_data_dir, exist_ok=True)

    # 1~50, 50~100위 웹페이지 주소
    url_chart_realtime = 'https://www.melon.com/chart/index.htm'

    #저장하기
    #'xt'모드와 try-except 모드를 쓸 경우
    file_path = os.path.join(path_data_dir, 'chart_realtime.html')
    try:
        file_mode = 'wt' if refresh_html else 'xt'
        with open(file_path, file_mode) as f:
            response = requests.get(url_chart_realtime)
            source = response.text
            f.write(source)
    except FileExistsError:
        print('File already exists!')

    x = open(file_path, 'rt')
    source = x.read()
    x.close()
    soup = BeautifulSoup(source, 'lxml')

    result = []
    for tr in soup.find_all('tr', class_=['lst50','lst100']):
        rank = tr.find('span', class_='rank').text
        title = tr.find('div', class_='rank01').find('a').text
        artist = tr.find('div', class_='rank02').find('a').text
        album = tr.find('div', class_='rank03').find('a').text
        url_img_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
        # http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/120/quality/80/optimize
        # .* -> 임의 문자의 최대 반복
        # \. -> '.' 문자
        # .*?/ -> '/'이 나오기 전까지의 최소 반복
        p = re.compile(r'(.*\..*?)/')
        url_img_cover = re.search(p, url_img_cover).group(1)

        result.append({
            'rank': rank,
            'title': title,
            'url_img_cover': url_img_cover,
            'artist': artist,
            'album': album,
        })
    return result