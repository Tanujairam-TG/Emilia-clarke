from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client,filters

@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="ππππππ π’πππ ππππππππ ππππ πππππ  π",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="π±ππΈπΆπ·π", callback_data="bright"),
                        InlineKeyboardButton(text="πΌπΈππ΄π³", callback_data="mix"),
                        InlineKeyboardButton(text="π± & π", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="π²πΈππ²π»π΄", callback_data="circle"),
                        InlineKeyboardButton(text="π±π»ππ", callback_data="blur"),
                        InlineKeyboardButton(text="π±πΎππ³π΄π", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="πππΈπ²πΊπ΄π", callback_data="stick"),
                        InlineKeyboardButton(text="ππΎππ°ππ΄", callback_data="rotate"),
                        InlineKeyboardButton(text="π²πΎπ½πππ°ππ", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="ππ΄πΏπΈπ°", callback_data="sepia"),
                        InlineKeyboardButton(text="πΏπ΄π½π²πΈπ»", callback_data="pencil"),
                        InlineKeyboardButton(text="π²π°πππΎπΎπ½", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="πΈπ½ππ΄ππ", callback_data="inverted"),
                        InlineKeyboardButton(text="πΆπ»πΈππ²π·", callback_data="glitch"),
                        InlineKeyboardButton(text="ππ΄πΌπΎππ΄-π±πΆ", callback_data="removebg"),
                    ],
                    [
                        InlineKeyboardButton(text="α΄Κα΄sα΄", callback_data="close_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
