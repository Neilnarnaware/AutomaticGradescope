import time

from selenium import webdriver
from selenium.webdriver import ActionChains

students = ["sbellu3@uic.edu","cchalk4@uic.edu","sfatim36@uic.edu","nhamda2@uic.edu","yhasna2@uic.edu","biden2@uic.edu","nirfan2@uic.edu","nlang6@uic.edu","elee232@uic.edu","slee664@uic.edu","ogonza21@uic.edu","tlung2@uic.edu","tmaato2@uic.edu","ynaray3@uic.edu","rodonn3@uic.edu","koye2@uic.edu","tqadri2@uic.edu","osalce3@uic.edu","ssheik30@uic.edu","ksusza2@uic.edu","ktu4@uic.edu","ruribe2@uic.edu","dvera9@uic.edu","rzadda2@uic.edu"]
driver_path = "E:\Setups\Selenium Chrome 85\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.maximize_window()



driver.refresh()
driver.get("https://www.gradescope.com/courses/81148")
time.sleep(10)
element_send = driver.find_element_by_id("session_email")
element_send.send_keys("nnarna2@uic.edu")
time.sleep(10)

element_send = driver.find_element_by_id("session_password")
element_send.send_keys("Sribalaji@02")
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/input").click()
time.sleep(10)
#driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/div[1]/a[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/section[2]/div/table/tbody/tr[4]/td[1]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div/a[1]").click()

for i in students:
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/main/section/div/strong/a").click()
    time.sleep(10)
    element_send = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[1]/label/input")

    element_send.send_keys(i)
    try:
        driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div[2]/table/tbody/tr/td[2]/a").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/main/div[2]/div[2]/div/div[2]/ol/li[1]/div/div/button").click()
        time.sleep(10)
    except:
        button = driver.find_element_by_xpath("        / html / body / nav[2] / div[1]").click()
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(button).click(button).perform()
        driver.find_element_by_xpath("/html/body/nav[1]/div[1]/ul[1]/li[3]/a/div[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[2]/div[1]/div/a[1]").click()
        continue

    time.sleep(10)

driver.close()
