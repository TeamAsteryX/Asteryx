# Copyright (C) 2021-present by TeamAsteryX@Github, < https://github.com/TeamAsteryX >.
#
# This file is part of < https://github.com/TeamAsteryX/Asteryx > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamAsteryX/Asteryx/blob/main/LICENSE >
#
# All rights reserved.


from Main import Altruix
from pyrogram import Client
import Main.core.types.message


if not hasattr(Client, "__send_custom__"):
    setattr(Client, "__send_custom__", Client.invoke)

import Main.core.types.client


if __name__ == "__main__":
    Altruix.run()
