from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
  driver.get("http://naver.com")

  element = driver.find_element(By.XPATH, "//*[@id='NM_FAVORITE']/div[1]/ul[2]/li[1]/a")
  print(element.text)
  
  image = driver.find_element(By.XPATH,"//*[@id='NM_MID_BANNER']/a[1]/span")
  print(image)
