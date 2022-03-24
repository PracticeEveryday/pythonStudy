from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
  driver.get("http://127.0.0.1:5500/test.html")

  # ol = driver.find_element_by_tag_name('ol')
  ol = driver.find_element(By.TAG_NAME, "ol")
  # li_list = ol.find_elements_by_tag_name('li')
  li_list = ol.find_elements(By.TAG_NAME, "li")
  for li in li_list:
    print(li.text)

  # big_list = driver.find_elements_by_class_name('big')
  big_list = driver.find_elements(By.CLASS_NAME, "big")

  for big in big_list:
    print(big.text)

  #ul = driver.find_element_by_tag_name('ul')
  ul = driver.find_element(By.TAG_NAME, "ul")
  # bold = ul.find_element_by_class_name('bold')
  bold = ul.find_element(By.CLASS_NAME, "bold")

  print(bold.text)