import config
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from FallenMusic import db_mem


def primary_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="🍻 sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_CHAT
            ),
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ 🍻", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ ᴍᴇɴᴜ ↺", callback_data=f"close"),
        ],
    ]
    return buttons


audio_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton("↻ ᴄʟᴏsᴇ ↺", callback_data="close")],
    ]
)


close_key = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")],
    ]
)
