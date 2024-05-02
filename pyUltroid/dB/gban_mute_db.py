# MerieUB - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

from .. import mdB


def list_gbanned():
    return mdB.get_key("GBAN") or {}


def gban(user, reason):
    ok = list_gbanned()
    ok.update({int(user): reason or "No Reason. "})
    return mdB.set_key("GBAN", ok)


def ungban(user):
    ok = list_gbanned()
    if ok.get(int(user)):
        del ok[int(user)]
        return mdB.set_key("GBAN", ok)


def is_gbanned(user):
    ok = list_gbanned()
    if ok.get(int(user)):
        return ok[int(user)]


def gmute(user):
    ok = list_gmuted()
    ok.append(int(user))
    return mdB.set_key("GMUTE", ok)


def ungmute(user):
    ok = list_gmuted()
    if user in ok:
        ok.remove(int(user))
        return mdB.set_key("GMUTE", ok)


def is_gmuted(user):
    return int(user) in list_gmuted()


def list_gmuted():
    return mdB.get_key("GMUTE") or []
