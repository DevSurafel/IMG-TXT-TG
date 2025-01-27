import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode  # Updated import for newer versions

# Replace with your bot's API token
API_TOKEN = '7387753841:AAHM0LJNVD8dYrxh-jWhxCogr5onXgZay_E'

# Replace with the chat ID where you want to send the message
CHAT_ID = '-1002033347065'

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
        await asyncio.sleep(180)  # Wait for 3 minutes

if __name__ == "__main__":
    asyncio.run(main())
