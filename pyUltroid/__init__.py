# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import os
import sys

from .version import __version__

run_as_module = __package__ in sys.argv or sys.argv[0] == "-m"


class ULTConfig:
    lang = "en"
    thumb = "resources/extras/ultroid.jpg"


if run_as_module:
    import time

    from .configs import Var
    from .startup import *
    from .startup._database import UltroidDB
    from .startup.BaseClient import UltroidClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import ultroid_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _ult_cache = {}
    _ignore_eval = []

    mdB = UltroidDB()
    update_envs()

    LOGS.info(f"Connecting to {mdB.name}...")
    if mdB.ping():
        LOGS.info(f"Connected to {mdB.name} Successfully!")

    BOT_MODE = mdB.get_key("BOTMODE")
    DUAL_MODE = mdB.get_key("DUAL_MODE")

    USER_MODE = mdB.get_key("USER_MODE")
    if USER_MODE:
        DUAL_MODE = False

    if BOT_MODE:
        if DUAL_MODE:
            mdB.del_key("DUAL_MODE")
            DUAL_MODE = False
        merie_bot = None

        if not mdB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        merie_bot = UltroidClient(
            validate_session(Var.SESSION, LOGS),
            mdB=mdB,
            app_version=ultroid_version,
            device_model="Ultroid",
        )
        merie_bot.run_in_loop(autobot())

    if USER_MODE:
        asst = merie_bot
    else:
        asst = UltroidClient("asst", bot_token=mdB.get_key("BOT_TOKEN"), mdB=mdB)

    if BOT_MODE:
        merie_bot = asst
        if mdB.get_key("OWNER_ID"):
            try:
                merie_bot.me = merie_bot.run_in_loop(
                    merie_bot.get_entity(mdB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder and asst._bot:
        merie_bot.run_in_loop(enable_inline(merie_bot, asst.me.username))

    vcClient = vc_connection(mdB, merie_bot)

    _version_changes(mdB)

    HNDLR = mdB.get_key("HNDLR") or "."
    DUAL_HNDLR = mdB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = mdB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("pyUltroid 2022 © TeamUltroid")

    from logging import getLogger

    LOGS = getLogger("pyUltroid")

    merie_bot = asst = mdB = vcClient = None
