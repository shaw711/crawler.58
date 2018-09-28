import re
import cv2
import time
import json
import requests
from io import BytesIO
import PIL.Image as image
from selenium import webdriver
from urllib.request import urlretrieve
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
browser.implicitly_wait(5)
wait = WebDriverWait(browser, 10)
browser.get("http://www.geetest.com/type/")
browser.find_elements_by_xpath("//div[@class='products-content']/ul/li")[1].click()
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "geetest_radar_tip")))
browser.find_elements_by_class_name("geetest_radar_tip")[1].click() if len(
    browser.find_elements_by_class_name("geetest_radar_tip")) > 1 else browser.find_element_by_class_name(
    "geetest_radar_tip").click()
time.sleep(2)
browser.find_element_by_class_name("geetest_refresh_1").click()
time.sleep(1)
refresh_url = browser.find_elements_by_css_selector("head script")[-1].get_attribute('src')
callback = requests.get(refresh_url).text
callback = json.loads(callback.split('(')[1].split(')')[0])
static_url = 'http://static.geetest.com/'
urlretrieve(url=static_url + callback['bg'], filename='../pic/bg.jpg')
print('缺口图片下载完成')
urlretrieve(url=static_url + callback['fullbg'], filename='../pic/fbg.jpg')
print('背景图片下载完成')

slider = browser.find_element_by_class_name("geetest_slider_button")
ActionChains(browser).click_and_hold(slider).perform()
ActionChains(browser).move_by_offset(120, yoffset=0).perform()
ActionChains(browser).release().perform()
time.sleep(2)
browser.close()

# imageDiv = browser.find_element_by_class_name("geetest_window")
# location = imageDiv.location
# size = imageDiv.size
# top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
# screen_shot = browser.get_screenshot_as_png()
# screen_shot = image.open(BytesIO(screen_shot))
# captcha = screen_shot.crop((left, top, right, bottom))
# captcha.save("../pic/screenshot.png")
#
# img_gray = cv2.imread("../pic/screenshot.png", cv2.IMREAD_GRAYSCALE)
# gradX = cv2.Sobel(img_gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
# gradY = cv2.Sobel(img_gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
# img_gradient = cv2.subtract(gradX, gradY)
# img_gradient = cv2.convertScaleAbs(img_gradient)
#
# blurred = cv2.blur(img_gradient, (9, 9))
# (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
# closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#
# closed = cv2.erode(closed, None, iterations=4)
# closed = cv2.dilate(closed, None, iterations=4)
#
# cv2.imshow('', closed)
# cv2.waitKey(3000)
# cv2.destroyAllWindows()
