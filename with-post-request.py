#nefiw79541@imdutex.com
#nefiw79541
import time
from Admitad_link_converter import link_convert, file_opener
import requests
from Aliexpress_scraper import Aliexpress_scraper
from test_telegram_bot import send_status_to_bot
counter_for_item = 0
counter_for_page = 1
error_counter = 0
def main_function(counter_for_item,counter_for_page,error_counter):
    item_list = ["Women Sweaters","Women Skirts","Women leggings","Women Jeans","Pajama sets","Hair accessories"
    ,"Dog toys","Costume shoes","Laptop batteries","Baby Shirts","Wedding Dresses","Scented Candles","Bluetooth Speaker","Smart Watch",
    "Neck massager","Portable Blender","Nail Polish","Wireless phone chargers","Doormats","Wifi repeater","Cat","Socks","Backpack","Baby Swings","Women blouses"]
    
    single_display_title,item_num,page_num = Aliexpress_scraper(item_list,counter_for_item,counter_for_page)
    counter_for_item,counter_for_page = item_num, page_num
    single_display_title = single_display_title.replace(" ","%20")
    images = file_opener("Image_URLS")
    for i in range(0,len(images)):
        images[i] = "https:" + images[i]
        
    displays = file_opener("Display_Titles")
    for i in range(0,len(displays)):
        displays[i] = displays[i].replace(" ","%20")
        displays[i] = single_display_title +"%20"+ displays[i]
        
    items = file_opener("Item-Urls")
    for i in range(0,len(items)):
        items[i] = link_convert(items[i])



    for i in range(0,int(len(items))):
        try:
            #account_post_list = []
            #THIS IS WHERE YOUR POST REQUEST WILL BE IN THE FORMAT BELOW
            """url = "https://www.pinterest.de/resource/PinResource/create"
            payload = f""
            headers = {
            }

            response = requests.request("POST", url, data=payload, headers=headers)"""


            """
            
            if account_post_list:
                account_post_list = " ".join(account_post_list)
                print("Following accounts have successfully posted their items: " + account_post_list)
                send_status_to_bot("Following accounts have successfully posted their items: " + account_post_list)
            else:
                print("Failed to post in every account")
                send_status_to_bot("Failed to post in every account")
            """
            if response.status_code != 200:
                print(str(i)+". posting failed" + "Reason: Request didn't pass")
                send_status_to_bot("DEVICE 1 "+str(i)+". Posting Failed" + "Reason: Request didn't pass")
                error_counter += 1
            else:
                send_status_to_bot("DEVICE 1 " +str(i)+". Post Created Succesfully" + "  Product Display Title: "+ displays[i][0:15])
                print(str(i)+". Post Created Succesfully" + "  Product Display Title: "+ displays[i][0:30])
            time.sleep(10300) 
                  
        except Exception as e:
            print(str(i)+". posting failed" + "Reason: "+ str(e))
            send_status_to_bot("DEVICE "+str(i)+". Posting Failed" + "Reason:" + str(e))
            #time.sleep(300)
            error_counter += 1
            time.sleep(10300) 
            pass
            
            
    return counter_for_item,counter_for_page,error_counter
if __name__ == "__main__":
    while True:
        counter_for_item,counter_for_page,error_counter = main_function(counter_for_item,counter_for_page,error_counter)

        