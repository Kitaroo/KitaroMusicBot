from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝗚𝗿𝗼𝘂𝗽 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝗚𝗿𝗼𝘂𝗽 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝗕𝗼𝗹𝗹𝘆𝘄𝗼𝗼𝗱",
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"𝗛𝗼𝗹𝗹𝘆𝘄𝗼𝗼𝗱",
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝗣𝗮𝗿𝘁𝘆",
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"𝗟𝗼𝗳𝗶",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝗦𝗮𝗱",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"𝘄𝗲𝗲𝗯",
                callback_data=f"play_playlist {user_id}|{type}|Weeb",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝗣𝘂𝗻𝗷𝗮𝗯𝗶",
                callback_data=f"play_playlist {user_id}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"𝗢𝘁𝗵𝗲𝗿𝘀",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝗚𝗼 𝗕𝗮𝗰𝗸",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ 𝘄𝗲𝗲𝗯",
                callback_data=f"add_playlist {videoid}|{type}|Weeb",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝗦𝗮𝗱",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ 𝗣𝗮𝗿𝘁𝘆",
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝗟𝗼𝗳𝗶",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ 𝗕𝗼𝗹𝗹𝘆𝘄𝗼𝗼𝗱",
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝗛𝗼𝗹𝗹𝘆𝘄𝗼𝗼𝗱",
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ 𝗣𝘂𝗻𝗷𝗮𝗯𝗶",
                callback_data=f"add_playlist {videoid}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"✚ 𝗢𝘁𝗵𝗲𝗿𝘀",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝘄𝗲𝗲𝗯", callback_data=f"check_playlist {type}|Weeb"
            ),
            InlineKeyboardButton(
                text=f"𝗦𝗮𝗱", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝗣𝗮𝗿𝘁𝘆", callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text=f"𝗟𝗼𝗳𝗶", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝗕𝗼𝗹𝗹𝘆𝘄𝗼𝗼𝗱",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"𝗛𝗼𝗹𝗹𝘆𝘄𝗼𝗼𝗱",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"𝗣𝘂𝗻𝗷𝗮𝗯𝗶",
                callback_data=f"check_playlist {type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"𝗢𝘁𝗵𝗲𝗿𝘀", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝗚𝗿𝗼𝘂𝗽 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]} 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"resumecb"),
            InlineKeyboardButton(text="II", callback_data=f"pausecb"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"skipcb"),
            InlineKeyboardButton(text="▢", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="𝗖𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗤𝘂𝗲𝘂𝗲𝗱 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁", url=f"{url}")],
        [InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]} {genre} 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="𝗖𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗤𝘂𝗲𝘂𝗲𝗱 𝗣𝗹𝗮𝘆𝗹𝗶𝘀𝘁t", url=f"{url}")],
        [InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"𝗬𝗲𝘀! 𝗗𝗲𝗹𝗲𝘁𝗲",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="𝗡𝗼!", callback_data=f"close"),
        ],
    ]
    return buttons
