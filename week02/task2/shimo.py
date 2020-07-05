from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()    
    browser.get('https://shimo.im')
    time.sleep(1)
    
    btm1 = browser.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]')
    btm1.click()

    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('shimirong@hotmail.com')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('Python123')
    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(@class,"sm-button")]').click()

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    browser.close()