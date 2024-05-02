# MerieUB - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

from .. import mdB


def get_stuff():
    return mdB.get_key("NOTE") or {}


def add_note(chat, word, msg, media, button):
    ok = get_stuff()
    if ok.get(int(chat)):
        ok[int(chat)].update({word: {"msg": msg, "media": media, "button": button}})
    else:
        ok.update({int(chat): {word: {"msg": msg, "media": media, "button": button}}})
    mdB.set_key("NOTE", ok)


def rem_note(chat, word):
    ok = get_stuff()
    if ok.get(int(chat)) and ok[int(chat)].get(word):
        ok[int(chat)].pop(word)
        return mdB.set_key("NOTE", ok)


def rem_all_note(chat):
    ok = get_stuff()
    if ok.get(int(chat)):
        ok.pop(int(chat))
        return mdB.set_key("NOTE", ok)


def get_notes(chat, word):
    ok = get_stuff()
    if ok.get(int(chat)) and ok[int(chat)].get(word):
        return ok[int(chat)][word]


def list_note(chat):
    ok = get_stuff()
    if ok.get(int(chat)):
        return "".join(f"👉 #{z}\n" for z in ok[chat])
