# -*- coding: utf-8 -*-

# Popup Dictionary Add-on for Anki
#
# Copyright (C)  2018-2019 Aristotelis P. <https://glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

# This file has been modified by lovac42 for CCBC, and is not the same as the original.


"""
Handles add-on configuration
"""

from __future__ import unicode_literals

import os
import io

from aqt import mw
from anki.utils import json

from .consts import *

defaults_path = os.path.join(addon_path, "config.json")
meta_path = os.path.join(addon_path, "meta.json")

def getConfig():
    return mw.addonManager.getConfig(__name__)

def writeConfig(config):
    mw.addonManager.writeConfig(__name__, config)


# initialize configuration. only performed at module load time for now
CONFIG = getConfig()
