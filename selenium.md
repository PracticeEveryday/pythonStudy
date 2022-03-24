# 사용 class_name:

button = driver.find_element_by_class_name("quiz_button")

button = driver.find_element(By.CLASS_NAME, "quiz_button")
비슷한 줄에서 다음도 변경해야 합니다.

# 사용 id:

element = find_element_by_id("element_id")

element = driver.find_element(By.ID, "element_id")

# 사용 name:

element = find_element_by_name("element_name")

element = driver.find_element(By.NAME, "element_name")

# 사용 link_text:

element = find_element_by_link_text("element_link_text")

element = driver.find_element(By.LINK_TEXT, "element_link_text")

# 사용 partial_link_text:

element = find_element_by_partial_link_text("element_partial_link_text")

element = driver.find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")

# 사용 tag_name:

element = find_element_by_tag_name("element_tag_name")

element = driver.find_element(By.TAG_NAME, "element_tag_name")

# 사용 css_selector:

element = find_element_by_css_selector("element_css_selector")

element = driver.find_element(By.CSS_SELECTOR, "element_css_selector")

# 사용 xpath:

element = find_element_by_xpath("element_xpath")

element = driver.find_element(By.XPATH, "element_xpath")
