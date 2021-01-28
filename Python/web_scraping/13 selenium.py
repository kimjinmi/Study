import time
from selenium import webdriver

# elem = browser.find_element_by_class_name("link_login")
# elem.click()

# elem = browser.find_element_by_id("query")

# from selenium.webdriver.common.keys import Keys 
# elem.send_keys("가나다")
# elem.send_keys(Keys.ENTER)

# elem = browser.find_elements_by_tag_name("a")

# for e in elem:
#     e.get_attribute("href") 

# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") 
# elem.click()

# browser.quit()

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

browser.find_element_by_id("log.login").click()

time.sleep(3)

# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

print(browser.page_source)
browser.quit() # 전체종료
#browser.clear() # 현재탭만 종료
