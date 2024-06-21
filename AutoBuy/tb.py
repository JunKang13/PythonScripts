import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buy_time(buytime):
    while True:
        if time.time() > buytime:
            if browser.find_element(By.ID, 'J_Go'):
                browser.find_element(By.ID, 'J_Go').click()
            print('抢购中')
            time.sleep(0.01)
            browser.find_element_by_link_text('提交订单').click()
            print('抢购成功')
            break

browser = webdriver.ChromeOptions()
browser.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
browser = webdriver.Chrome(chrome_options=browser)

browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 3)
if browser.find_element_by_link_text('亲，请登录'):
    browser.find_element_by_link_text('亲，请登录').click()
    print('请在15秒内完成扫码')
    time.sleep(5)

browser.get('https://cart.taobao.com/cart.htm')
wait = WebDriverWait(browser, 5)

if browser.find_element(By.ID, 'J_SelectAll1'):
    browser.find_element(By.ID, 'J_SelectAll1').click()
    # select_all()

buytime = time.time() + 600
buy_time(buytime)
# time.sleep(10)

