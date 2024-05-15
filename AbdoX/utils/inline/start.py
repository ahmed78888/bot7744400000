from pyrogram.types import InlineKeyboardButton

import config
from AbdoX import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url= "https://t.me/PO_UV"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مطور السورس ", url=f"https://t.me/DAD_E3DAM"),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/PO_UV"), 
        ],
        [
            
            InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=f"https://t.me/CG_G11") , 
        ],
    ]
    return buttons
