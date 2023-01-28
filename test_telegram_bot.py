import telebot
import requests
Api_Key = "YOUR API"
chat_id = "YOUR CHAT ID"

def send_status_to_bot(yess):
    response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(Api_Key, "sendMessage"),
            data={'chat_id': chat_id, 'text': yess}
        ).json()
    return True
