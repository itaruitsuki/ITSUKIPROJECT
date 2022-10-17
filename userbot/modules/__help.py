#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Recode by Fariz <Github.com/farizjs>
#    From Flicks-Userbot
#    <t.me/TheFlicksUserbot>


from userbot import BOT_USERNAME, CMD_HELP, bot
from userbot.utils import edit_or_reply, edit_delete, alby_cmd

user = bot.get_me()
DEFAULTUSER = user.first_name


@alby_cmd(pattern="help ?(.*)")
async def cmd_list(event):
    if args := event.pattern_match.group(1).lower():
        if args in CMD_HELP:
            await edit_or_reply(
                event,
                f"**❖ Commands available in {args} ❖** \n\n{str(CMD_HELP[args])}"
                + "\n\n**☞ @ruangprojects**",
            )

        else:
            await edit_delete(event, f"**Module** `{args}` **Tidak tersedia!**")
    else:
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@KyyUserbot"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException:
            await edit_delete(event,
                              f"**INLINE MODE KAMU BELUM AKTIF!!**\n** Silahkan Ikuti Tutorial dibawah ini Untuk Menyalakan Inline Mode Kamu.**\n\n**© Tutorial Untuk Menyalakan Inline Mode Kamu :**\n**❖ Silahkan pergi ke bot @BotFather ketikan** '/mybots'\n**❖ Kemudian pilih bot Assistant mu yang ada di group log**\n**❖ Lalu pilih Bot Settings > Pilih inline Mode > pilih Turn on**\n**❖ Setelah itu Pergi ke group log atau group ini lagi**\n**Ketik** `.helpme` **lagi untuk membuka menu bantuan modules nya.**"
                              )
