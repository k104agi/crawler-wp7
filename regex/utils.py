import re
import requests


__all__ = (
    'get_tag_attriue',
    'get_tag_content',
)


def save():
    """멜론 인기차트 50위까지 페이지를 melon.html에 저장함
    :return: None
    """
    response = requests.get('https://www.melon.com/chart/index.htm')
    source = response.text
    with open('melon.html', 'wt') as f:
        f.write(source)


def get_tag_attribute(attribute_name, tag_string):
    """
    특정 tag문자열(tag_string)에서 attribute_name에 해당하는 속성의 값을 리턴하는 함수
    :param attribute_name: 태그가 가진 속성명
    :return: 속성이 가진 값
    """
    # 문자열 포맷에 이름 붙이고, format()에서 키워드인수로 전달
    p = re.compile(r'^<.*?{attribute_name}="(?P<value>.*?)".*?>'.format(
        attribute_name=attribute_name
    ), re.DOTALL)
    m = re.search(p, tag_string)
    if m:
        return m.group('value')
    return ''


# example1 = '<a href="https://google.co.kr">Google</a>'
example1 = '<div><span class="sdf">ASDF</span></div>'
get_tag_attribute('href', example1)


def get_tag_content(tag_string):
    """
    특정 tag문자열(tag_string)이 가진 내용을 리턴
    tag문자열이 스스로 열고 닫는 태그 (ex: img태그)일 경우엔 공백을 반환
    :param tag_string:
    :return:
    """

def find_tag(tag, tag_string):
    """
    tag_string에서 tag 요소를 찾아 리턴
    :param tag: 찾을 tag명
    :param tag_string: 검색할 tag 문자열
    :return: 첫번째로 찾은 tag명
    """
    p = re.compile(r'.*?(<{tag}.*?{class_}.*?>.*?</{tag}>)'.format(
        tag=tag, class_=f'class=".*?{class_}.*?"' if class_ else '',
    ), re.DOTALL)
    print(f'find_Tag (tag: {tag}, class')
