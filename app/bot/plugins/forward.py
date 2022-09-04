from pyrogram import filters
from pyrogram.types import Message
from bot import JunctionBot
from config import Config
from ..utils import forward_message


def forward_filter(_, __, m: Message):
    return any(m.chat.id == chats for chats in Config.JUNCTION_CHATS)


@JunctionBot.on_message(filters.create(forward_filter) & filters.incoming)
async def _(c: JunctionBot, m: Message):
    await forward_message(c, m)
