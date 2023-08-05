#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from threading import Thread
import time
import traceback
import flet as ft


import os

from .chat.chat import main



def WEB(host_data, port_data):

    ft.app(target=main, view=ft.AppView.WEB_BROWSER, host=host_data,
           port=port_data, assets_dir=os.path.join(os.path.dirname(__file__), "assets"))
