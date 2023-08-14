#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
from kot import KOT

from naruno.apps.remote_app import Integration

import time
import fire
import pickle
import contextlib

database = KOT("database")
database_new_messages = KOT("database_new_messages")

secret = KOT("secret")

settings = KOT("settings")
user_db = KOT("user_db", folder=os.path.join(os.path.dirname(__file__)))

class web3:
    command_line = False
    def __init__(self, port=8000, host="localhost", hour=None,):
        if hour != None:
            settings.set("hour", hour)

        self.integration = None
        self.host = host
        self.port = port

        self.official = "c923c646f2d73fcb8f626afacb1a0ade8d98954a"


    @property
    def post_wait_time(self):
        record = settings.get("hour")
        if record == None:
            record = 24
        return record * 60 * 60


    def set_pass(self, password:str):
        secret.set("password", password)

    
    def user_final(self):
        if web3.command_line:
            self.close()            
        return True        


    def auth_need(self):
        if self.integration is None:
            password = secret.get("password")
            self.integration = Integration("Web3", password=password, port=self.port, host=self.host)

    def username(self, username:str):
        self.auth_need()
        if len(username) > 15:
            self.user_final()
            raise Exception("Username should be max 15 char")
        self.integration.send("username", username, self.official)
        return self.user_final()
    
    def post(self, post:str):
        self.auth_need()
        last_post = user_db.get("last_post")
        if last_post is not None and time.time() - last_post < self.post_wait_time:
            self.user_final()
            raise Exception("You cant send more post.")
        if len(post) > 100:
            self.user_final()
            raise Exception("Post should be max 100 char")
        if self.integration.send("post", post, self.official):
            user_db.set("last_post", time.time())
        return self.user_final()

    def get_user(self, username:str):
        record = database.get(username)
        if record == None:
            record = {"username": username, "posts": None, "last_post": 0, "post_numer":0}
        return record


    def run(self):
        while True:
            data = self.integration.get()
            if data != []:
                for each in data:
                    user = each["fromUser"]
                    action = each["data"]["action"].replace("Web3","")
                    data = each["data"]["app_data"]



                    control = True

                    if not isinstance(data, str):
                        control = False
                    if not isinstance(user, str):
                        control = False
                    
                    if action not in ["username", "post"]:
                        control = False

                    if action == "username":
                        if len(data) > 15:
                            control = False
                        record = database.get_all()
                        for _user in record:
                            if record[_user]["username"] == data:
                                control = False
                    elif action == "post":
                        if len(data) > 100:
                            control = False
                        if time.time() - self.get_user(user)["last_post"] < self.post_wait_time:
                            control = False
                        
                    
                    if control:

                        database_user = self.get_user(user)

                        if action == "username":
                            database_user["username"] = data
                        elif action == "post":
                            database_user["posts"] = data
                            database_user["last_post"] = time.time()
                            database_user["post_numer"] += 1
                            database_new_messages.set(each["signature"], [database_user["username"], data])

                        database.set(user, database_user)



            time.sleep(5)

    def close(self):
        self.integration.close()


class web3_web:
    @staticmethod
    def web(host=None, port=0):
        from .gui import WEB
        WEB(host, port)


def main():
    web3.command_line = True
    fire.Fire(web3)

def web_main():
    fire.Fire(web3_web)
