import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\selenium webdriver\chromedriver.exe")
driver.get("https://www.desmos.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"(//a[text()='Graphing Calculator'])[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='dcg-btn-flat-gray dcg-show-keypad dcg-do-not-blur']").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[17]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//div[@class='dcg-keypad-btn-container'])[6]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[19]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//div[@class='dcg-keypad-btn-container'])[15]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='dcg-minimize-keypad']").click()
time.sleep(3)
driver.save_screenshot("C:\screenshot\One.png")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='dcg-btn-flat-gray dcg-show-keypad dcg-do-not-blur']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='dcg-keypad-btn dcg-btn-short-blue']").click()        #blue
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[1]").click()     #x
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[17]").click()     #=
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[4]").click()      #fuction
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-gray'])[2]").click()      #cos
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[4]").click()    #fuction
time.sleep(3)
driver.find_element(By.XPATH,"(//div[@class='dcg-keypad-btn-container'])[14]").click()      #5
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[7]").click()     #)
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[18]").click()    #+
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[11]").click()   #2
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[2]").click()    #y
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[4]").click()     #function
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-gray'])[5]").click()   #sec
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[4]").click()  #function
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[15]").click()      #0
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[7]").click()  #)
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='dcg-minimize-keypad']").click()
time.sleep(3)
driver.save_screenshot("C:\screenshot\Two.png")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='dcg-btn-flat-gray dcg-show-keypad dcg-do-not-blur']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='dcg-keypad-btn dcg-btn-short-blue']").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[17]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[6]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[4]").click()
time.sleep(3)
flag=driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-gray'])[77]")
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-gray'])[77]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[11]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[9]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//div[@class='dcg-keypad-btn-container'])[16]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[8]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[7]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[14]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-dark-on-gray'])[11]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//span[@class='dcg-keypad-btn dcg-btn-light-on-gray'])[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='dcg-minimize-keypad']").click()
time.sleep(3)
driver.save_screenshot("C:\screenshot\Three.png")
time.sleep(3)
driver.close()



