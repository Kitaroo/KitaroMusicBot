from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="𝗦𝗲𝗮𝗿𝗰𝗵 𝗟𝘆𝗿𝗶𝗰𝘀",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ 𝗬𝗼𝘂𝗿 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="✚ 𝗚𝗿𝗼𝘂𝗽 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬇️ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗔𝘂𝗱𝗶𝗼/𝗩𝗶𝗱𝗲𝗼",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝗚𝗼 𝗕𝗮𝗰𝗸",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝗖𝗹𝗼𝘀𝗲",
                callback_data=f"close",
            )
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝗚𝗲𝘁 𝗔𝘂𝗱𝗶𝗼",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝗚𝗲𝘁 𝗩𝗶𝗱𝗲𝗼",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data=f"close"),
        ],
    ]
    return buttons
