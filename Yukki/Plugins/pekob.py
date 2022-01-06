import os
from aiohttp import ClientSession
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, InputMediaVideo
from Python_ARQ import ARQ 
from asyncio import get_running_loop
from wget import download
from Yukki import app


ARQ_API_KEY = "SOURZI-MLCGOE-NQQBCM-MOWHFZ-ARQ"

session = ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, session)
pornhub = arq.pornhub
phdl = arq.phdl


db = {}


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


async def download_url(url: str):
    loop = get_running_loop()
    file = await loop.run_in_executor(None, download, url)
    return file


async def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":")))
    )


@app.on_message(filters.command(["phub", "pornhub"]))
async def sarch(_,message):
    search = get_text(message)
    m = await message.reply_text(f"getting {search} from server...")
    try:
        resp = await pornhub(search,thumbsize="large")
        res = resp.result
    except:
        await m.edit("not found: 404")
        return
    if not resp.ok:
        await m.edit("not found, try again")
        return
    resolt = f"""
**🏷 Title:** {res[0].title}
**⏱️ Duration:** {res[0].duration}
**👀 Views:** {res[0].views}
**🌟 Rating:** {res[0].rating}"""
    await m.delete()
    m = await message.reply_photo(
        photo=res[0].thumbnails[0].src,
        caption=resolt,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("▶️ Next",
                                         callback_data="next"),
                    InlineKeyboardButton("🗑 Close",
                                         callback_data="delete"),
                ],
                [
                    InlineKeyboardButton("📥 Download",
                                         callback_data="dload")
                ]
            ]
        ),
        parse_mode="markdown",
    )
    new_db={"result":res,"curr_page":0}
    db[message.chat.id] = new_db


@app.on_callback_query(filters.regex("next"))
async def callback_query_next(_, query):
    m = query.message
    try:
        data = db[query.message.chat.id]
    except:
        await m.edit("something went wrong.. **try again**")
        return
    res = data['result']
    curr_page = int(data['curr_page'])
    cur_page = curr_page+1
    db[query.message.chat.id]['curr_page'] = cur_page
    if len(res) <= (cur_page+1):
        cbb = [
                [
                    InlineKeyboardButton("◀️ Prev",
                                         callback_data="previous"),
                    InlineKeyboardButton("📥 Download",
                                         callback_data="dload"),
                ],
                [
                    InlineKeyboardButton("🗑 Close",
                                         callback_data="delete"),
                ]
              ]
    else:
        cbb = [
                [
                    InlineKeyboardButton("◀️ Prev",
                                         callback_data="previous"),
                    InlineKeyboardButton("▶️ Next",
                                         callback_data="next"),
                ],
                [
                    InlineKeyboardButton("🗑 Close",
                                         callback_data="delete"),
                    InlineKeyboardButton("📥 Download",
                                         callback_data="dload")
                ]
              ]
    resolt = f"""
**🏷 Title:** {res[cur_page].title}
**⏱️ Duration:** {res[curr_page].duration}
**👀 Views:** {res[cur_page].views}
**🌟 Rating:** {res[cur_page].rating}"""

    await m.edit_media(media=InputMediaPhoto(res[cur_page].thumbnails[0].src))
    await m.edit(
        resolt,
        reply_markup=InlineKeyboardMarkup(cbb),
        parse_mode="markdown",
    )


@app.on_callback_query(filters.regex("previous"))
async def callback_query_next(_, query):
    m = query.message
    try:
        data = db[query.message.chat.id]
    except:
        await m.edit("something went wrong.. **try again**")
        return
    res = data['result']
    curr_page = int(data['curr_page'])
    cur_page = curr_page-1
    db[query.message.chat.id]['curr_page'] = cur_page
    if cur_page != 0:
        cbb=[
                [
                    InlineKeyboardButton("◀️ Prev",
                                         callback_data="previous"),
                    InlineKeyboardButton("▶️ Next",
                                         callback_data="next"),
                ],
                [
                    InlineKeyboardButton("🗑 Close",
                                         callback_data="delete"),
                    InlineKeyboardButton("📥 Download",
                                         callback_data="dload")
                ]
            ]
    else:
        cbb=[
                [
                    InlineKeyboardButton("▶️ Next",
                                         callback_data="next"),
                    InlineKeyboardButton("🗑 Close",
                                         callback_data="Delete"),
                ],
                [
                    InlineKeyboardButton("📥 Download",
                                         callback_data="dload")
                ]
            ]
    resolt = f"""
**🏷 Title:** {res[cur_page].title}
**⏱️ Duration:** {res[curr_page].duration}
**👀 Views:** {res[cur_page].views}
**🌟 Rating:** {res[cur_page].rating}"""

    await m.edit_media(media=InputMediaPhoto(res[cur_page].thumbnails[0].src))
    await m.edit(
        resolt,
        reply_markup=InlineKeyboardMarkup(cbb),
        parse_mode="markdown",
    )

    
@app.on_callback_query(filters.regex("dload"))
async def callback_query_next(_, query):
    m = query.message
    data = db[m.chat.id]
    res = data['result']
    curr_page = int(data['curr_page'])
    dl_links = await phdl(res[curr_page].url)
    db[m.chat.id]['result'] = dl_links.result.video
    db[m.chat.id]['thumb'] = res[curr_page].thumbnails[0].src
    db[m.chat.id]['dur'] = res[curr_page].duration
    resolt = f"""
**🏷 Title:** {res[curr_page].title}
**⏱️ Duration:** {res[curr_page].duration}
**👀 Views:** {res[curr_page].views}
**🌟 Rating:** {res[curr_page].rating}"""
    pos = 1
    cbb = []
    for resolts in dl_links.result.video:
        b= [InlineKeyboardButton(f"{resolts.quality} - {resolts.size}", callback_data=f"phubdl {pos}")]
        pos += 1
        cbb.append(b)
    cbb.append([InlineKeyboardButton("Delete", callback_data="delete")])
    await m.edit(
        resolt,
        reply_markup=InlineKeyboardMarkup(cbb),
        parse_mode="markdown",
    )

    
@app.on_callback_query(filters.regex(r"^phubdl"))
async def callback_query_dl(_, query):
    m = query.message
    capsion = m.caption
    entoty = m.caption_entities
    await m.edit(f"**downloading...** :\n\n{capsion}")
    data = db[m.chat.id]
    res = data['result']
    curr_page = int(data['curr_page'])
    thomb = await download_url(data['thumb'])
    durr = await time_to_seconds(data['dur'])
    pos = int(query.data.split()[1])
    pos = pos-1
    try:
        vid = await download_url(res[pos].url)
    except Exception as e:
        print(e)
        await m.edit("download error..., try again")
        return
    await m.edit(f"**Upload Sekarang** :\n\n{capsion}")
    await app.send_chat_action(m.chat.id, "upload_video")
    await m.edit_media(media=InputMediaVideo(vid,thumb=thomb, duration=durr, supports_streaming=True))
    await m.edit_caption(caption=capsion, caption_entities=entoty)
    if os.path.isfile(vid):
        os.remove(vid)
    if os.path.isfile(thomb):
        os.remove(thomb)
    

@app.on_callback_query(filters.regex("delete"))
async def callback_query_delete(_, query):
    await query.message.delete()
