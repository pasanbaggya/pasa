from pyrogram.types import Message
from bot import JunctionBot
from config import Config


async def forward_message(c: JunctionBot, m: Message):
    for chat in Config.JUNCTION_CHATS:
        if chat != m.chat.id:
            await c.forward_messages(
                chat,
                m.chat.id,
                message_ids=m.message_id
            )