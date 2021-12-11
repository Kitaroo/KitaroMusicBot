from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import BOT_USERNAME


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝗛𝗲𝗹𝗽𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗠𝗲𝗻𝘂", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝗛𝗲𝗹𝗽𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗠𝗲𝗻𝘂", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝗛𝗲𝗹𝗽𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗠𝗲𝗻𝘂", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝗛𝗲𝗹𝗽𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗠𝗲𝗻𝘂", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 𝗦𝗲𝘁𝘁𝗶𝗻𝗴𝘀", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝗛𝗲𝗹𝗽𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗠𝗲𝗻𝘂", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝗛𝗲𝗹𝗽𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗠𝗲𝗻𝘂", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝗛𝗲𝗹𝗽𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗠𝗲𝗻𝘂", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 𝗛𝗲𝗹𝗽𝗲𝗿 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗠𝗲𝗻𝘂", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 𝗔𝘂𝗱𝗶𝗼 𝗤𝘂𝗮𝗹𝗶𝘁𝘆", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 𝗔𝘂𝗱𝗶𝗼 𝗩𝗼𝗹𝘂𝗺𝗲", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 𝗨𝘀𝗲𝗿𝘀 𝗟𝗶𝘀𝘁𝘀", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 𝗗𝗮𝘀𝗵𝗯𝗼𝗮𝗿𝗱", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ 𝗖𝗹𝗼𝘀𝗲", callback_data="close"),
            InlineKeyboardButton(text="🔙 𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 𝗥𝗲𝘀𝗲𝘁 𝗔𝘂𝗱𝗶𝗼 𝗩𝗼𝗹𝘂𝗺𝗲 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 𝗟𝗼𝘄 𝗩𝗼𝗹", callback_data="LV"),
            InlineKeyboardButton(text="🔉 𝗠𝗲𝗱𝗶𝘂𝗺 𝗩𝗼𝗹", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 𝗛𝗶𝗴𝗵 𝗩𝗼𝗹", callback_data="HV"),
            InlineKeyboardButton(text="🔈 𝗔𝗺𝗽𝗹𝗶𝗳𝗶𝗲𝗱 𝗩𝗼𝗹", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 𝗖𝘂𝘀𝘁𝗼𝗺 𝗩𝗼𝗹𝘂𝗺𝗲 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼𝗖𝘂𝘀𝘁𝗼𝗺 𝗩𝗼𝗹𝘂𝗺𝗲 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 𝗘𝘃𝗲𝗿𝘆𝗼𝗻𝗲", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 𝗔𝗱𝗺𝗶𝗻𝘀", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 𝗨𝘀𝗲𝗿𝘀 𝗟𝗶𝘀𝘁𝘀", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ 𝗨𝗽𝘁𝗶𝗺𝗲", callback_data="UPT"),
            InlineKeyboardButton(text="💾 𝗥𝗮𝗺", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 𝗖𝗽𝘂", callback_data="CPT"),
            InlineKeyboardButton(text="💽 𝗗𝗶𝘀𝗸", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 𝗚𝗼 𝗕𝗮𝗰𝗸", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons
