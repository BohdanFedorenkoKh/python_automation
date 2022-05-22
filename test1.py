from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

text_field = browser.find_element_by_id("answer").send_keys(y)

checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
checkbox.click()
checkbox2 = browser.find_element_by_css_selector("[for='robotsRule']")
checkbox2.click()
submit = browser.find_element_by_css_selector("button.btn.btn-default").click()

