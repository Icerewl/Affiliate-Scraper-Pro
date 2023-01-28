from itertools import product
import requests
import pandas
import time
import csv
import sys
from test_telegram_bot import send_status_to_bot

def Aliexpress_scraper(item_listas,counter_for_item,counter_for_page):
    

    proxy = "173.245.49.47:80"
    url = "https://www.aliexpress.com/glosearch/api/product"
    payload = ""
    img_Url_list = []
    display_Title_list = []
    item_Url_list = []

    """
    s = sys.argv


    s = s[1:-1]

    listToStr = ' '.join([str(elem) for elem in s])
    """
    #print(str(counter_for_page)+"Program başlarken sayfa sayısı bu")
    for counter in range(1):
        time.sleep(1)
        querystring = {"trafficChannel":"main","d":"y","CatId":"0","SearchText":item_listas[counter_for_item],"ltype":"wholesale","SortType":"default","page":counter_for_page,"origin":"y","pv_feature":"1005004732290926,1005003496017478,1005003448490073,1005003424842769,1005003831538969,1005004338833281,1005004453035700,1005001490865918,1005004673584342,1005004248508059,1005003227263359,1005004592233669,1005004527477439,1005004279828609,1005004229753492,1005003081448148,4001253513692,1005004765392040,1005004715460791,4001194328609,1005004526511246,1005004437722660,4000176695736,1005004778883043,1005004379486862,1005004446351746,1005004779818613,4000977620476,1005004148917391,32926952018,1005004779860517,1005004085764652,1005003117573638,1005004765217009,1005003936282923,1005002679058945,1005004141794266,1005003777444354,1005002785054245,1005003461992493"}

        payload = ""
        headers = {
            "YOUR HEADERS GOES HERE"
        }
        #, proxies={'http': proxy, 'https': proxy}, timeout=3
        try:
            #, proxies={'http':proxy, 'https':proxy},timeout=3
            response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        except requests.exceptions.ProxyError:
            print("proxy is shit")
            send_status_to_bot("Proxy is shit my man")
            
            exit(1)

        data = response.json()
        
        #print(response.status_code)
        for i in range(0,59):
            #Url_list = []
            #Url_list.append()
            
            img_Url_list.append(data["mods"]["itemList"]["content"][i]["image"]["imgUrl"].replace("220x220","Q90"))
            #print(data["mods"])
            #display_Title_list.append(data["mods"]["itemList"]["content"][i]["title"]["displayTitle"])
            display_Title_list.append(data["mods"]["itemList"]["content"][i]["image"]["imgUrl"].split("/")[-1][:-18].replace("-"," "))
            item_Url_list.append("https://www.aliexpress.com/item/" +data["mods"]["itemList"]["content"][i]["productId"]+ ".html")
            #print(data["mods"]["itemList"]["content"][i]["image"]["imgUrl"])
            #print(data["mods"]["itemList"]["content"][i]["title"]["displayTitle"])
        #["mods"]["itemList"]["content"][0]
    returning_display_title = item_listas[counter_for_item]
    if counter_for_page == 1:
        counter_for_page = 2
        #print(str(counter_for_page)+ "counter for page bu") 
    elif counter_for_page == 2:
        #print("buraya gir di mi diye merak ediyorum")
        counter_for_item += 1
        counter_for_page = 1  


    with open("Image_URLS", 'w', newline='',encoding="utf-8") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(img_Url_list)
        
    with open("Display_Titles", 'w', newline='',encoding="utf-8") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(display_Title_list)

    with open("Item-Urls",'w', newline='',encoding="utf-8") as abx:
        wr = csv.writer(abx, quoting=csv.QUOTE_ALL)
        wr.writerow(item_Url_list)
    
    print("Aliexpress data has successfully scraped")
    send_status_to_bot("Aliexpress data has successfully scraped")
    return returning_display_title,counter_for_item,counter_for_page