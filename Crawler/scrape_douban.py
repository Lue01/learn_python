import requests
from bs4 import BeautifulSoup

# 加入请求头，伪装成浏览器，以绕过网站的反爬机制
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"}
for num in range(0,250,25):
    response=requests.get(f"https://movie.douban.com/top250?start={num}",headers=headers)
    # print(response)
    # print(response.status_code)
    # print(response.content)
    # print(response.text)

    content=response.text
    soup=BeautifulSoup(content,'html.parser')
    # print(soup)

    all_titles=soup.find_all("span",attrs={"class":"title"})
    # print(all_titles)
    for title in all_titles:
        title_string=title.string
        if "/" not in title_string:
            print(title_string)