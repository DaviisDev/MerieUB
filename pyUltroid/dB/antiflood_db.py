# MerieUB - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.


from .. import mdB


def get_flood():
    return mdB.get_key("ANTIFLOOD") or {}


def set_flood(chat_id, limit):
    omk = get_flood()
    omk.update({chat_id: limit})
    return mdB.set_key("ANTIFLOOD", omk)


def get_flood_limit(chat_id):
    omk = get_flood()
    if chat_id in omk.keys():
        return omk[chat_id]


def rem_flood(chat_id):
    omk = get_flood()
    if chat_id in omk.keys():
        del omk[chat_id]
        return mdB.set_key("ANTIFLOOD", omk)
