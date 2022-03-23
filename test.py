from selenium import webdriver

with webdriver.Chrome() as driver:
  driver.get("http://127.0.0.1:5500/test.html")

  ol = driver.find_element_by_tag_name('ol')
  li_list = ol.find_elements_by_tag_name('li')

  for li in li_list:
    print(li.text)

  big_list = driver.find_elements_by_class_name('big')

  for big in big_list:
    print(big.text)

  ul = driver.find_element_by_tag_name('ul')
  bold = ul.find_element_by_class_name('bold')

  print(bold.text)