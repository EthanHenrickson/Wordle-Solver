import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def init():
    global driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://wordwiz.com/new")
    time.sleep(3)
    elem = driver.find_element(By.CLASS_NAME, 'btn-close')
    elem.click()

def sendKeysToParse(word):
    elem = driver.find_element(By.CSS_SELECTOR, "body")
    for item in word:
        elem.send_keys(item)
    elem.send_keys(Keys.RETURN)
    time.sleep(4.5)
    return color()

def color():
    tempList = []
    elem = driver.find_elements(By.CLASS_NAME,'flip-back')
    try:
        jic = driver.find_element(By.CLASS_NAME,'wp-cell-invalid').value_of_css_property('color')
        if jic == "rgb(247, 79, 120)":
            backward()
            return tempList
    except:
        pass

    for item in elem[len(elem)-5:]:
        elem2 = item.value_of_css_property('background-color')
        if elem2 == "rgb(158, 159, 180)":
            tempList.append(0)
        elif elem2 == "rgb(255, 176, 0)":
            tempList.append(1)
        elif elem2 == "rgb(143, 201, 65)":
            tempList.append(2)
        
    return tempList

def backward():
    elem = driver.find_element(By.CSS_SELECTOR,"body")
    for item in range(5):
        elem.send_keys(Keys.BACKSPACE)

def close():
    driver.close()
        



    


#color = driver.find_element(By.CLASS_NAME,"wp-cell-present").value_of_css_property('background-color')
#print(color)



#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#driver.close()