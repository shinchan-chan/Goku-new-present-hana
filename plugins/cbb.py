from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"<b>Premium Benefits & Perks\nDirect Channel Links, No Ad Links\nSpecial Access In Events\n\nPricing Rates\n1 Months - INR 99\n3 Months - INR 249\n6 Months - INR 499\n9 Months - INR 699\n12 Months - INR 999\n\nWant To Buy?\nPay Using Crypto\nSend Screenshot to @DoraShin_hlo\n\nWe Have Limited Seats For Premium Users</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/DoraShin_hlo"),
                        InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/HellFire_Movies")
                    ],
                    [
                        InlineKeyboardButton("Anime", url="https://t.me/HellFire_Academy"),
                        InlineKeyboardButton("Ongoing Anime", url="https://t.me/Ongoing_HellFire_Academy")
                    ],
                    [
                        InlineKeyboardButton("ʜᴀɴɪᴍᴇ&ʜ*ɴᴛᴀɪ", url="https://t.me/Adult_Flux"),
                        InlineKeyboardButton("🔒ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass