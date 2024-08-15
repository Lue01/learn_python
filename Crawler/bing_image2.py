import os
import time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# 设置搜索关键词和Bing图片搜索URL
search_query = "夏季服装穿搭"
url = f"https://www.bing.com/images/search?q={search_query}&form=HDRSC2"

# 设置保存图片的目录
save_dir = "C:\\yoloimg\\clothe2"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 设置要下载的图片数量
num_images = 1000
downloaded_images = 0

# 设置EdgeDriver的路径
edge_driver_path = "C:\\Users\\Secrecy\\AppData\\Local\\Programs\\Python\\Python312\\MicrosoftWebDriver.exe"  # 替换为实际路径
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)

# 打开浏览器并访问URL
driver.get(url)
time.sleep(2)  # 等待页面加载

# 滚动页面加载更多图片
while downloaded_images < num_images:
    # 获取页面中所有图片的缩略图
    thumbnail_images = driver.find_elements(By.CSS_SELECTOR, "img.mimg")
    
    for thumbnail in thumbnail_images:
        try:
            # 点击缩略图，打开高清图片页面
            driver.execute_script("arguments[0].click();", thumbnail)
            time.sleep(2)  # 等待页面加载高清图片
            
            # 查找高清图片，通过 `img[src]` 来获取图片 URL
            full_image = driver.find_element(By.CSS_SELECTOR, "img[src]")
            img_url = full_image.get_attribute("src")
            
            # 构建图片保存路径
            img_name = f"{downloaded_images+1}.jpg"
            img_path = os.path.join(save_dir, img_name)
            
            # 下载并保存图片
            urlretrieve(img_url, img_path)
            print(f"Downloaded: {img_name}")
            downloaded_images += 1
        except Exception as e:
            print(f"Failed to download image {downloaded_images+1}: {e}")

        if downloaded_images >= num_images:
            break
    
    # 滚动页面以加载更多图片
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 等待加载

# 关闭浏览器
driver.quit()

print(f"Downloaded {downloaded_images} images to {save_dir}")
