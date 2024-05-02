# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

from .. import mdB


def get_muted():
    return mdB.get_key("MUTE") or {}


def mute(chat, id):
    ok = get_muted()
    if ok.get(chat):
        if id not in ok[chat]:
            ok[chat].append(id)
    else:
        ok.update({chat: [id]})
    return mdB.set_key("MUTE", ok)


def unmute(chat, id):
    ok = get_muted()
    if ok.get(chat) and id in ok[chat]:
        ok[chat].remove(id)
    return mdB.set_key("MUTE", ok)


def is_muted(chat, id):
    ok = get_muted()
    return bool(ok.get(chat) and id in ok[chat])
