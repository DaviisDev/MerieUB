# MerieUB - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.


from .. import mdB


def get_stuff(key="NSFW"):
    return mdB.get_key(key) or {}


def nsfw_chat(chat, action):
    x = get_stuff()
    x.update({chat: action})
    return mdB.set_key("NSFW", x)


def rem_nsfw(chat):
    x = get_stuff()
    if x.get(chat):
        x.pop(chat)
        return mdB.set_key("NSFW", x)


def is_nsfw(chat):
    x = get_stuff()
    if x.get(chat):
        return x[chat]


def profan_chat(chat, action):
    x = get_stuff("PROFANITY")
    x.update({chat: action})
    return mdB.set_key("PROFANITY", x)


def rem_profan(chat):
    x = get_stuff("PROFANITY")
    if x.get(chat):
        x.pop(chat)
        return mdB.set_key("PROFANITY", x)


def is_profan(chat):
    x = get_stuff("PROFANITY")
    if x.get(chat):
        return x[chat]
