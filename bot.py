import os
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
IMAGE_PATH = 'tg.jpg'

if not API_TOKEN or not CHAT_ID:
    raise ValueError("BOT_TOKEN or CHAT_ID is missing in environment variables.")

MESSAGE_TEXT = (
    "Akkamiin Add gochuu dandeenya? \n\n"
    "1) Maqaa garee kanaa tuqaa ☝️ \n\n"
    "2) 👤 Add Members kan jedhu tuquun yoo xiqqaate nama 200 add gochuun qarshii 10,000 badhaafamaa. \n\n"
    "Kan add gootan baayyina nama Add gootanii barreessaa. Ergasii asiin nu qunnamuun lakkoofsa account baankii keessanii nuuf ergaa:\n\n"
    '<a href="https://t.me/Digital_Birr_Bot?start=ar6222905852">'
    "🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁\n"
    "🎁🎁🎁 10,000 ETB 🎁🎁🎁🎁\n"
    "🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁</a>\n\n"
    "DIGITAL BIRR - BY ETHIOPIAN AIRLINES ✈️\n\n"
)

async def send_message_with_image(bot):
    try:
        contact_button = InlineKeyboardButton("Add Bank Account ➕", url="https://t.me/Digital_Birr_Bot?start=ar6222905852")
        keyboard = InlineKeyboardMarkup([[contact_button]])

        # Ensure the image file exists before sending
        if not os.path.exists(IMAGE_PATH):
            raise FileNotFoundError(f"Image file '{IMAGE_PATH}' not found.")

        with open(IMAGE_PATH, 'rb') as photo:
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=photo,
                caption=MESSAGE_TEXT,
                parse_mode=ParseMode.HTML,
                reply_markup=keyboard
            )
        print("Message sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    bot = Bot(token=API_TOKEN)
    while True:
        await send_message_with_image(bot)
        await asyncio.sleep(200)

if __name__ == "__main__":
    asyncio.run(main())
