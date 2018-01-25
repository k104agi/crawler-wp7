import requests
import re
import save_melon


source = open('melon.html', 'rt').read()


PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank02">(.*)</div>', re.DOTALL)

PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')


#m = re.findall(r'(?<=재생">).*?(?=</a>)', source)
#if m:
#    print(m)

match_list = re.finditer(PATTERN_DIV_RANK01, source)
for match_div_rank01 in match_list:
    div_rank01_content = match_div_rank01.group()

    match_title = re.search(PATTERN_A_CONTENT, div_rank01_content)
    title = match_title.group(1)
    print(title)

#PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank02">(.*)</div>', re.DOTALL)
#div_rank01 = re.search(PATTERN_DIV_RANK01, source).group()
#print(div_rank01)

#PATTER_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
#title = re.search(PATTER_A_CONTENT, div_rank01).group(1)
#print(title)

#save_melon.save(title)

#p = re.compile(r'<a.*?>')
#result = re.findall(pattern_div_rank01, source)
#for index, item in enumerate(result):
#    print(index, item)

#p = re.compile(r'<a.*?>')
#result = re.findall(p, source)r
#for index, item in enumerate(result):
#    print(index, item)