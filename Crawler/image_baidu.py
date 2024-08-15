import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.request import urlretrieve

# 设置搜索关键词和Bing图片搜索URL
search_query = "夏季服装穿搭图片"
encoded_query = quote(search_query)
base_url = f"https://www.bing.com/images/search?q={encoded_query}&form=HDRSC2&first=1&tsc=ImageBasicHover"

# 设置保存图片的目录
save_dir = "C:\\yoloimg\\clothe_bing"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 设置要下载的图片数量
num_images = 1000
downloaded_images = 0
page = 0

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

while downloaded_images < num_images:
    # 更新URL以处理分页
    page += 1
    url = f"{base_url}&first={page*30}"

    # 发送请求并解析网页内容
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # 获取所有图片的标签
    img_tags = soup.find_all("img", class_="mimg")

    for img_tag in img_tags:
        img_url = img_tag.get("src")
        if not img_url:
            img_url = img_tag.get("data-src")  # 处理懒加载图片

        if img_url and downloaded_images < num_images:
            try:
                # 构建图片保存路径
                img_name = f"{downloaded_images + 1}.jpg"
                img_path = os.path.join(save_dir, img_name)

                # 下载并保存图片
                urlretrieve(img_url, img_path)
                print(f"Downloaded: {img_name}")
                downloaded_images += 1
            except Exception as e:
                print(f"Failed to download image {downloaded_images + 1}: {e}")

        if downloaded_images >= num_images:
            break

    if not img_tags:  # 如果没有更多的图片，则退出循环
        print("No more images found.")
        break

print(f"Downloaded {downloaded_images} images to {save_dir}")
