import os
import time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 设置搜索关键词和Bing图片搜索URL
search_query = "夏季服装穿搭"
url = f"https://www.bing.com/images/search?q={search_query}&form=HDRSC2"

# 设置保存图片的目录
save_dir = "C:\\yoloimg\\clothe3"
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
    # 找到所有缩略图
    thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.mimg")  # 可能需要根据实际情况调整
    for thumbnail in thumbnails:
        if downloaded_images >= num_images:
            break

        try:
            # 点击缩略图以查看高清图片
            ActionChains(driver).move_to_element(thumbnail).click().perform()
            time.sleep(2)  # 等待高清图片加载

            # 获取高清图片的URL
            img_elements = driver.find_elements(By.XPATH,  "//span[contains(@class, 'adjacentContainer')]//img[@class='nofocus']")
            for img_element in img_elements:
                if downloaded_images >= num_images:
                    break

                try:
                    # 获取高清图片的URL
                    img_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'imgContainer')]//img"))
                    )
                    img_url = img_element.get_attribute("src")

                    if img_url:
                        # 构建图片保存路径
                        img_name = f"{downloaded_images + 1}.jpg"
                        img_path = os.path.join(save_dir, img_name)

                        # 下载并保存图片
                        urlretrieve(img_url, img_path)
                        print(f"Downloaded: {img_name}")
                        downloaded_images += 1

                except Exception as e:
                    print(f"Failed to download image {downloaded_images + 1}: {e}")

            # 关闭高清图片视图
            try:
                close_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.close"))
                 )
                close_button.click()
                time.sleep(1)  # 等待关闭动画
                    
            except Exception as e:
                print(f"Failed to close image view: {e}")

        except Exception as e:
            print(f"Failed to download image {downloaded_images + 1}: {e}")

    # 滚动页面以加载更多图片
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 等待加载

# 关闭浏览器
driver.quit()

print(f"Downloaded {downloaded_images} images to {save_dir}")
