
from time import sleep
from telethon import TelegramClient

api_id = 8398003
api_hash = 'b30a91d6e8101c2bec980598aaa7280e'

dest = input('Enter number with "+" or id with "@"')

client = TelegramClient('me', api_id, api_hash)
async def main():
    mail = 'test'
    while (mail != '*'):
        mail = input()
        mes = await client.send_message(dest, ".")
        i = 1
        while(i <= len(mail)):
            while(mail[i-1] == ' '):
                i += 1
            await client.edit_message(dest, mes.id, mail[:i])
            i += 1
            sleep(0.1)
with client:
    client.loop.run_until_complete(main())