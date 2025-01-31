import os
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode  
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

IMAGE_PATH = 'tg.jpg'

MESSAGE_TEXT = (
    "Akkamiin Add gochuu dandeenya? \n\n"
    "👤 Add Members kan jedhu tuquun yoo xiqqaate nama 200 add gochuun qarshii 10,000 badhaafamaa. \n\n"
    "Kan add gootan asiin 👉[Contact](https://t.me/Digital_Birr_Bot?start=ar6222905852) nu qunnamuun lakkoofsa account baankii keessanii nuuf ergaa \n\n"
    "DIGITAL BIRR - BY ETHIOPIAN AIRLINES ✈️\n\n"
)

async def send_message_with_image():
    try:
        bot = Bot(token=API_TOKEN)

        contact_button = InlineKeyboardButton("Add Bank Account ➕", url="https://t.me/Digital_Birr_Bot?start=ar6222905852")
        keyboard = InlineKeyboardMarkup([[contact_button]])

        await bot.send_photo(
            chat_id=CHAT_ID,
            photo=open(IMAGE_PATH, 'rb'),
            caption=MESSAGE_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard
        )
        print("Message sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    while True:
        await send_message_with_image()
        await asyncio.sleep(300) 

if __name__ == "__main__":
    asyncio.run(main())
