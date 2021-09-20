from telethon.sync import TelegramClient
import os
from os import system
import time

api_id = #enter here api id
api_hash = '' #enter here api hash
num = '' #phone number
client = TelegramClient(num, api_id, api_hash)

os.system('cls||clear')
client.connect()
client.send_code_request(num)
client.sign_in(num, input('Code: '))

while True:
    client.send_message("put here username of the target" ,"put here message")
