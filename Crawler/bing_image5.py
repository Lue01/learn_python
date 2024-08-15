import os
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置保存图片的目录
save_dir = "C:\\yoloimg\\clothe5"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 设置要下载的图片数量
num_images = 400
downloaded_images = 259

# 设置EdgeDriver的路径
edge_driver_path = "C:\\Users\\Secrecy\\AppData\\Local\\Programs\\Python\\Python312\\MicrosoftWebDriver.exe"  # 替换为实际路径
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)

# 记录已经处理过的图片URL
downloaded_urls = set()

# 打开浏览器并访问URL
url = "https://cn.bing.com/images/search?q=%E5%A4%8F%E5%AD%A3%E7%A9%BF%E6%90%AD&qs=n&form=QBIR&sp=-1&lq=0&pq=%E5%A4%8F%E5%AD%A3%E7%A9%BF%E6%90%AD&sc=10-4&cvid=946A6AE87A6F427FA4C0BCBDB9E1F3ED&ghsh=0&ghacc=0&first=1"
driver.get(url)
time.sleep(2)  # 等待页面加载

def download_image(img_url, img_path):
    try:
        req = Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as response, open(img_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded: {img_path}")
    except HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason} for {img_url}")
        if e.code == 420:
            print("Rate limit hit, waiting before retrying...")
            time.sleep(60)  # 等待60秒后重试
            download_image(img_url, img_path)  # 递归重试
    except URLError as e:
        print(f"URLError: {e.reason} for {img_url}")
    except Exception as e:
        print(f"Failed to download image: {e}")

# 滚动页面加载更多图片
while downloaded_images < num_images:
    thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.mimg")
    for thumbnail in thumbnails:
        if downloaded_images >= num_images:
            break

        # 获取缩略图的URL
        thumbnail_url = thumbnail.get_attribute("src")
        if thumbnail_url in downloaded_urls:
            continue  # 如果已经处理过，跳过这个缩略图

        try:
            # 点击缩略图以查看高清图片
            ActionChains(driver).move_to_element(thumbnail).click().perform()
            time.sleep(2)  # 等待高清图片加载
            
            iframe = driver.find_element(By.XPATH, "//iframe[@id='OverlayIFrame']")
            driver.switch_to.frame(iframe)

            # 获取高清图片的URL
            img_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'imgContainer')]//img"))
            )
            img_url = img_element.get_attribute("src")

            if img_url:
                # 构建图片保存路径
                img_name = f"{downloaded_images + 1}.jpg"
                img_path = os.path.join(save_dir, img_name)

                # 下载并保存图片
                download_image(img_url, img_path)
                downloaded_images += 1
                downloaded_urls.add(thumbnail_url)  # 记录已经处理的URL

            # 关闭高清图片视图
            close_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.close"))
            )
            close_button.click()
            time.sleep(1)  # 等待关闭动画
            driver.switch_to.default_content()

        except Exception as e:
            print(f"Failed to download image {downloaded_images + 1}: {e}")

    # 滚动页面以加载更多图片
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)  # 等待加载

# 关闭浏览器
driver.quit()

print(f"Downloaded {downloaded_images} images to {save_dir}")
