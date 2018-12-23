import requests
from bs4 import BeautifulSoup

"""
1.請求部份
"""

# 向ptt的server請求網頁
res = requests.post("https://www.ptt.cc/bbs/joke/M.1545234824.A.951.html")

# 拿取回傳的html文字
html = res.text

"""
2.解析部份
"""

# 把html丟進解析器，利用lxml方法解析
soup = BeautifulSoup(html, 'lxml')

# 解析出所有推文物件
all_push = soup.find_all('div', {'class':'push'})

# 一個一個解析推文並印在控制台
for push in all_push:

    # 解析推噓
    # 推文的class是hl push-tag
    tag = push.find('span', {'class':'hl push-tag'})
    if not tag:
        # 噓文的class是f1 hl push-tag
        tag = push.find('span', {'class':'f1 hl push-tag'})
    tag = tag.get_text()


    # 解析user ID
    user_id = push.find('span', {'class':'f3 hl push-userid'}).get_text()

    # 解析推文內容
    content = push.find('span', {'class':'f3 push-content'}).get_text()

    # 解析更新時間
    time = push.find('span', {'class':'push-ipdatetime'}).get_text()

    # 印出推文資訊
    print("{} {}: {}\n\t{}".format(tag, user_id, content, time))