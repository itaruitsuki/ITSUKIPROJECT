# This is a troll indeed ffs *facepalm*
# Ported from xtra-telegram by @heyworld
import asyncio
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
#from userbot.utils import admin_cmd
from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP, bot

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.fgban(?: |$)(.*)")
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = f"`Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By` {DEFAULTUSER}\n"
    await event.edit("**Summoning out the mighty gban hammer ☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1036951071:
            await reply_message.reply("`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 6969$ to my master__ [Heyworld](tg://user?id=1036951071) __to release your account__😏")
        else:
            firstname = replied_user.user.first_name
            jnl = ("`Warning!!`"
                   "[{}](tg://user?id={})"
                   f"` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By` {DEFAULTUSER}\n\n"
                   "**Name: ** __{}__\n"
                   "**ID : ** `{}`\n"
                   ).format(firstname, idd, firstname, idd)
            usname = replied_user.user.username
            if usname is None:
                jnl += "**Username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += f"**Username** : @{usname}\n"
            if len(gbunVar) > 0:
                gbunm = f"`{gbunVar}`"
                gbunr = f"**Reason: **{gbunm}"
                jnl += gbunr
            else:
                no_reason = "No Reason Given "
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = (
            f"Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By {DEFAULTUSER} \nReason: No Reason Given. ")
        await event.reply(mention)
    await event.delete()

CMD_HELP.update({
    "fakegban": "`.fgban`\
    \nUsage: Type .fgban or Reply .fgban reason and see it yourself. "
})
