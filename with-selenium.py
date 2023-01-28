from base64 import encode
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from Admitad_link_converter import link_convert,file_opener
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import pathlib
import time
from selenium.webdriver.common.proxy import Proxy, ProxyType
import sys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from test_telegram_bot import send_status_to_bot
from Aliexpress_scraper import Aliexpress_scraper
from selenium.webdriver.common.action_chains import ActionChains


current_directory = pathlib.Path(__file__).parent.resolve()
item_list = ["Women Sweaters","Women Skirts","Women leggings","Women Jeans","Pajama sets","Hair accessories"
,"Dog toys","Costume shoes","Laptop batteries","Baby Shirts","Wedding Dresses","Scented Candles","Bluetooth Speaker","Smart Watch",
"Neck massager","Portable Blender","Nail Polish","Wireless phone chargers","Doormats","Wifi repeater","Cat","Socks","Backpack","Baby Swings","Women blouses"]

def open_selenium():
    options = FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 15)
    return driver,wait






def image_downloader(driver,wait,counter_for_item,counter_for_page):
    single_display_title,item_num,page_num = Aliexpress_scraper(item_list,counter_for_item,counter_for_page)
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    images = file_opener("Image_URLS")
    for i in range(0,len(images)):
        images[i] = "https:" + images[i]
    counter_for_image = 0
    for i in range(len(images)):
        if counter_for_image >= len(images):
            break
        
        a = str(current_directory) + r"\images\image{}.png".format(counter_for_image)
        
        encoderus_var = "cp1251"
        try:
            
            urllib.request.urlretrieve(images[counter_for_image],a)
        except UnicodeEncodeError:
            exception_handle = images[counter_for_image].decode(encoderus_var)
            urllib.request.urlretrieve(exception_handle,a)

        driver.get(images[counter_for_image])
        print("Succesfully downloaded: "+ str(counter_for_image)+ "."+images[counter_for_image])
        send_status_to_bot("Succesfully downloaded: "+ str(counter_for_image)+". Image")
        counter_for_image += 1
    return single_display_title,item_num,page_num

    

def pinterest_general(single_display_titlas,driver,wait):
    actions = ActionChains(driver)
    displays = file_opener("Display_Titles")
    items = file_opener("Item-Urls")
    for i in range(0,len(items)):
        items[i] = link_convert(items[i])
    driver.get("https://www.pinterest.de/login/")
    email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
    password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    email.send_keys("Your credentials")
    password.send_keys("Your Credentials")
    time.sleep(3/2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[3]/form/div[7]/button').click()
    time.sleep(3)
    driver.get("https://www.pinterest.de/pin-builder/")

    #len(file_opener("Image_URLS"))
    for i in range(0,6):
        

        description_area = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/textarea')))
        description_area.send_keys(items[i])
        title_area = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/textarea')
        title_area.send_keys(single_display_titlas)
        #title_area.click()
        actions.send_keys(Keys.TAB)
        actions.send_keys(single_display_titlas + " " +displays[i])
        actions.perform()
        #second_title_area = driver.find_element(By.CSS_SELECTOR, "span[data-text='true']")
        #second_title_area.send_keys(single_display_titlas + displays[i])
        upload = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/input')
        upload.send_keys(str(current_directory) + r"\images\image{}.png".format(i))
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]'))).click()
                                                                                                               
        try:
         
            wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button"))).click()
         
            print(str(i)+". Post Created Succesfully" + "  Product Display Title: "+ displays[i][0:30])
            send_status_to_bot(str(i)+". Post Created Succesfully" + "  Product Display Title: "+ displays[i][0:15])
        except Exception as e:
            print(str(i)+". posting failed" + "Reason: "+ str(e))
            print(e)
            send_status_to_bot(str(i)+". Posting Failed" + "Reason:" + str(e))
        
        driver.get("https://www.pinterest.de/pin-builder/")
        time.sleep(300)
         
def main():
    counter_for_item = 0
    counter_for_page = 1
    while True:
        driver,wait = open_selenium()
        
        single_display_titlas,item_num,page_num = image_downloader(driver,wait,counter_for_item,counter_for_page)
        counter_for_item,counter_for_page = item_num, page_num
           
        pinterest_general(single_display_titlas,driver,wait)
        driver.quit()
    

if __name__ == "__main__":
    main()
    