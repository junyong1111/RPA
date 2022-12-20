import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
browser.get("https://www.naver.com")

browser.find_element(By.ID, "id").send_keys("ID")
#-- 입력 데이터 지우기
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("ID")

browser.find_element(By.ID, "pw").send_keys("PW")
browser.find_element(By.ID, "pw").send_keys(Keys.ENTER)

#-- html 정보 출력

print(browser.page_source)
# browser.close() #-- 현재 탭만 종료
browser.quit() #-- 브라우저 전체 종료

time.sleep(5.0)


