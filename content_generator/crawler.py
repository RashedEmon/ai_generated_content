import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import openai
from PIL import Image
from bs4 import BeautifulSoup


class Crawler:
    def __int__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 3)

    def run(self, caption_list):
        index = 1
        for caption in caption_list:
            images = self.get_images(caption)
            for image in images:
                try:
                    self.wait.until(ec.element_to_be_clickable(image)).click()
                    selected_image = self.wait.until(
                        ec.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'KAlRDb')]")))
                    src = selected_image.get_attribute("src")
                    img_type = src.split(".")
                    img_type = img_type[len(img_type) - 1]
                    # print(img_type)
                    if img_type in ['jpg', 'jpeg', 'png', 'webp']:
                        response = requests.get(src)
                        if response.status_code == 200:
                            with open(f"../services/images/image_{index}.png", "wb") as file:
                                file.write(response.content)
                                break
                except Exception as e:
                    print(e)
            index += 1

    def get_images(self, image_caption):
        search_text = f"{image_caption} image png or jpg format"
        search_text.split(" ")
        "+".join(search_text)
        self.driver.get(
            f"https://www.google.com/search?q={search_text}&client=ubuntu&hs=Iav&channel=fs&source=lnms&tbm=isch&sa=X"
            f"&ved=2ahUKEwjBys34p_T8AhXR_3MBHRD4AFgQ_AUoAnoECAEQBA&biw=1846&bih=968&dpr=1")
        search_images = self.driver.find_elements(By.XPATH, "//*[@id='islrg']/div[1]/div//*[contains(@class, 'rg_i')]")

        return search_images

    def add_seo_content_into_image(self, text):
        for i in range(1, 3):
            img = Image.open(f"../services/images/image_{i}.png")
            img.info["Description"] = text
            img.info["Title"] = "title"
            img.save(f"../services/images/image_{i}.png", "png", quality=95, optimize=True, progressive=True)
