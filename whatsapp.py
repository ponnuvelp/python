import datetime
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(r'C:\Users\ponnuvex\Desktop\Chrome\Application\chromedriver.exe')
driver_1=driver
driver.get('https://web.whatsapp.com/')
msg='I am happy to inform you Good morning:) this is my first software to send automatic message to friends by setting time'
input('Enter anything after scanning QR code')
#contact=input('enter the contact')
name=['C Manjunath']
i=1
#name =['5']
for buddy in name:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(buddy))
    user.click()
    delay=5
    #try:
        #msg_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"_13mgZ" )))
        #mes_box.click()

    msg_box = driver.find_element_by_class_name("_13mgZ")
    """if contact == "group":
        edit=driver.find_element_by_class_name("_19RFN")
        edit.send_keys("ponnuvel")"""
        #msg_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, '_3FeAD _1PRhq')))
    print("Sending messages---->>!")
    #except TimeoutException:
    #    print ("Loading took too much time!")
    #    driver.quit()
    while 1:
        date_time = datetime.datetime.now()
        #date = date_time.date()  # Gives the date
        time_1 = date_time.time()  # Gives the time
        time.sleep(1)
        #print (date.year, date.month, date.day)
        print (time_1.hour, time_1.minute, time_1.second, time_1.microsecond)
        if time_1.hour==0 and time_1.minute ==13 and time_1.second==0:
            break

        if time_1.hour==0 and time_1.minute ==12 and time_1.second>1:
            msg_1=msg+str(i)
            msg_box.send_keys(i)
            driver.find_element_by_class_name("_3M-N-").click()
            i=i+1
            print("Task completed ")
            print(buddy)


msg_box.send_keys(msg)
driver.find_element_by_class_name("_3M-N-").click()
driver_1.quit()
