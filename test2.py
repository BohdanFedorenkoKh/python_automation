from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

box = browser.find_element_by_id("treasure").get_attribute("valuex")
name = calc(box)
label_answer = browser.find_element_by_id("answer").send_keys(name)
check_box = browser.find_element_by_id("robotCheckbox").click()
radio_button = browser.find_element_by_id("robotsRule").click()
submit = browser.find_element_by_css_selector("button.btn.btn-default").click()


