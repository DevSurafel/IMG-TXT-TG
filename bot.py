import os
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode  # Updated import for newer versions
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the bot token and chat ID from environment variables
API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Replace with the file path of the image
IMAGE_PATH = 'tg.jpg'

# Replace with the message text
MESSAGE_TEXT = (
    "Akkamiin Add gochuu dandeenya? \n\n"
    "👤 Add Members kan jedhu tuquun yoo xiqqaate nama 200 add gochuun qarshii 10,000 badhaafamaa. \n\n"
    "Kan gootan asiin 👉[Contact](https://t.me/Digital_Birr_Bot?start=ar6222905852) nu qunnamuun badhaasa keessan fudhadhaa"
)

async def send_message_with_image():
    try:
        # Initialize the bot
        bot = Bot(token=API_TOKEN)

        # Create an inline keyboard with the Contact button
        contact_button = InlineKeyboardButton("Contact", url="https://t.me/Digital_Birr_Bot?start=ar6222905852")
        keyboard = InlineKeyboardMarkup([[contact_button]])

        # Send the image with the message text and the inline button
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
        await asyncio.sleep(300)  # Wait for 5 minutes

if __name__ == "__main__":
    asyncio.run(main())
