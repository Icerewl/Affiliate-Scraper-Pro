# Affiliate Scraper Pro

###### Affiliate Scraper Pro is a bot that helps users earn affiliate income with ease. The bot scrapes product information and images from Aliexpress.com, transforms the links to the user's affiliate link through admitad.com, and then automatically shares those products on Pinterest.com.

###### This bot streamlines the process of finding and sharing products, allowing users to focus on growing their affiliate income.

## How it works
1.The bot starts by importing the necessary modules, including time, requests, and the custom modules Admitad_link_converter, Aliexpress_scraper, and test_telegram_bot.

2.The main_function is defined, which takes in three parameters: counter_for_item, counter_for_page, and error_counter.

3.Within main_function, a list of items to be scraped from Aliexpress.com is defined. The Aliexpress_scraper function is then called, passing in the item list, counter_for_item, and counter_for_page. This function returns the scraped product information and images.

4.The scraped image URLs and item URLs are then modified to include the user's affiliate link through the link_convert function.

5.The bot then uses the requests module to make a POST request to Pinterest.com, sharing the scraped products on the user's account.

6.The bot continues this process, looping through the list of items and sharing them on the user's Pinterest account. If there is an error in the process, the error is logged and the error_counter is incremented.

7.The main_function returns the updated counter_for_item, counter_for_page, and error_counter values.

8.The bot runs indefinitely in a while loop, continuously calling main_function and updating the counters as necessary.

## Requirements:
Python 3
requests library
Admitad account
Pinterest account
# Getting started:
Clone the repository
Install the required libraries
Run the main.py file
Set up telegram bot for sending the status to your telegram account
Update the credentials and tokens for Admitad and Pinterest account
Run the code and wait for the products to be posted on your Pinterest account
## Note:
There is a sleep time of 10300 seconds(2.9 hours) after each request to avoid suspension from Pinterest.
## Customization:
The code is highly customizable to match the user's needs. Users can change the items to be scraped, the number of items scraped per page, and the sleep time between requests.

## Conclusion:
Affiliate Scraper Pro is a powerful tool that helps users automate the process of finding and sharing products on Pinterest, allowing them to focus on growing their affiliate income. With its easy-to-use interface and customizable options, users can quickly start earning affiliate income with minimal effort.
