# 로컬 HTML문서 불러오기
source = open('melon.html', 'rt').read()



PATTERN_TD = re.compile(r'<td.*?>.*?</td>', re.DOTALL)

td_ist = re.findall(PATTERN_TD, source)

for index, td in enumerate(td_list):
    td_strip = re.sub(r'[\n\t]+', '', td)
    print(f'{index:02}: {td_strip}')



example2 = '<div>Content</div>'
get_tag_content(example2)
# -> Content


# 전체 문서에서 PATTERN_DIV_RANK01에 해당하는 match object목록을 순회
match_list = re.finditer(PATTERN_DIV_RANK01, source)
for match_div_rank01 in match_list:
    # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
    div_rank01_content = match_div_rank01.group()

    # 부분 문자열에서 a태그의 내용을 title변수에 할당
    match_title = re.search(PATTERN_A_CONTENT, div_rank01_content)
    title = match_title.group(1)
    print(title)



#match_list = re.finditer(PATTERN_IMG_URL, source)
#for match_url in match_list:
#    img_url = match_url.group()
#
#    match_title = re.search(PATTERN_SONG_NAME, img_url)
#    title = match_title.group(1)
#    print(title)
